"""Live execution adapter (§14) — OFF by default, gated three ways.

Nothing here runs unless all three gates are open:

1. `LIVE_ENABLED=True` in config. Defaults False.
2. A **static-IP preflight** that compares the current WAN IP against the
   registered one and refuses on mismatch. Order APIs require a registered
   static IP; discovering that at the exchange's rejection is worse than
   discovering it here.
3. An **interactive typed confirmation** per rebalance, echoing the total
   notional and the order count. Not a y/n — the operator types a token that
   contains the notional, so a reflexive "yes" cannot arm a trade they did not
   read.

§14 is also explicit that automatic IP re-registration is NOT to be built. It
would be a way of routing around a broker control, and whether it is within
intended use is a question for the broker rather than something to assume. The
adapter reports the mismatch and stops.

§2 forbids auto-rebalancing on a schedule without explicit human confirmation.
Gate 3 is that confirmation, and it cannot be satisfied programmatically —
`confirm_fn` exists so tests can drive it, and a caller passing a lambda that
returns the token has disabled their own safety, visibly, in their own code.
"""
from __future__ import annotations

import datetime as dt
from typing import Any, Callable

import requests

from src.config import Config, get_config
from src.execution.adapter import ExecutionAdapter, ExecutionResult, Fill
from src.portfolio.rebalance import RebalancePlan

DHAN_API = "https://api.dhan.co/v2"
IP_LOOKUP_URLS = ("https://api.ipify.org", "https://checkip.amazonaws.com")


class LiveExecutionBlocked(RuntimeError):
    """A gate refused. The message says which one and what to do about it."""


class DhanLiveAdapter(ExecutionAdapter):
    name = "dhan_live"
    is_live = True

    def __init__(
        self,
        config: Config | None = None,
        *,
        session: requests.Session | None = None,
        confirm_fn: Callable[[str], str] | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self.config = config or get_config()
        self.session = session or requests.Session()
        self.confirm_fn = confirm_fn or (lambda prompt: input(prompt))
        self._token_provider = token_provider

    # -- gates -------------------------------------------------------------

    def _assert_enabled(self) -> None:
        if not self.config.live_enabled:
            raise LiveExecutionBlocked(
                "LIVE_ENABLED is False. Live execution is off by default (§14). "
                "Set LIVE_ENABLED=True in .env only when you intend to trade "
                "real money, and expect to type a confirmation per rebalance."
            )

    def current_wan_ip(self) -> str | None:
        for url in IP_LOOKUP_URLS:
            try:
                response = self.session.get(url, timeout=10)
                if response.status_code < 400:
                    return response.text.strip()
            except requests.RequestException:
                continue
        return None

    def preflight(self, plan: RebalancePlan) -> list[str]:
        """Every check that must pass before an order is sent."""
        problems = super().preflight(plan)
        self._assert_enabled()

        registered = self.config.registered_static_ip
        if not registered:
            problems.append(
                "DHAN_REGISTERED_IP is not set. Order APIs require a registered "
                "static IP; without knowing it, the preflight cannot verify "
                "anything and must not pass."
            )
        else:
            current = self.current_wan_ip()
            if current is None:
                problems.append(
                    "could not determine the current WAN IP, so the static-IP "
                    "requirement cannot be verified"
                )
            elif current != registered:
                problems.append(
                    f"WAN IP {current} does not match the registered static IP "
                    f"{registered}. Orders will be rejected by the broker. "
                    "Re-register the IP with Dhan manually — this platform "
                    "deliberately does not automate IP re-registration (§14); "
                    "whether that is within intended use is a question for the "
                    "broker, not an assumption to make in code."
                )

        if plan.blocked_orders:
            problems.append(
                f"{len(plan.blocked_orders)} orders are for circuit-locked names "
                "and cannot execute at the quoted price"
            )
        return problems

    def _confirm(self, plan: RebalancePlan) -> None:
        """Interactive typed confirmation echoing notional and order count (§14)."""
        summary = plan.summary()
        token = f"TRADE-{summary['n_orders']}-{int(round(summary['total_notional']))}"
        prompt = (
            "\n" + "=" * 66 + "\n"
            + plan.confirmation_text()
            + "\n" + "=" * 66 + "\n"
            + "This will place REAL orders with REAL money.\n"
            + f"To proceed, type exactly:  {token}\n> "
        )
        answer = (self.confirm_fn(prompt) or "").strip()
        if answer != token:
            raise LiveExecutionBlocked(
                "confirmation token did not match; no orders were placed. "
                "The token encodes the order count and total notional so that "
                "confirming requires reading them."
            )

    # -- execution ---------------------------------------------------------

    def execute(self, plan: RebalancePlan, **kwargs: Any) -> ExecutionResult:
        problems = self.preflight(plan)
        if problems:
            raise LiveExecutionBlocked(
                "live execution preflight failed:\n  - " + "\n  - ".join(problems)
            )
        self._confirm(plan)

        token = self._access_token()
        result = ExecutionResult(adapter=self.name, plan_date=plan.as_of_date)
        executed_at = dt.datetime.now(tz=dt.timezone.utc).isoformat()

        for order in plan.orders:
            payload = {
                "transactionType": order.side.upper(),
                "exchangeSegment": "NSE_EQ",
                "productType": "CNC",          # delivery, per the cost model
                "orderType": "LIMIT",
                "validity": "DAY",
                "securityId": order.isin,
                "quantity": int(order.quantity),
                "price": float(order.price),
            }
            try:
                response = self.session.post(
                    f"{DHAN_API}/orders",
                    headers={"access-token": token, "Content-Type": "application/json"},
                    json=payload, timeout=30,
                )
            except requests.RequestException as exc:
                result.rejected.append((order, f"network error: {exc}"))
                continue

            if response.status_code >= 400:
                result.rejected.append((order, f"HTTP {response.status_code}"))
                continue

            body = _safe_json(response)
            result.fills.append(Fill(
                isin=order.isin, symbol=order.symbol, side=order.side,
                quantity=order.quantity, price=order.price,
                notional=order.notional, cost_total=order.estimated_cost,
                cost_items={"estimated": order.estimated_cost},
                executed_at=executed_at, order_id=str(body.get("orderId", "")),
                # The broker acknowledges receipt, not execution. Calling this
                # "filled" would overstate what we know.
                status="acknowledged",
            ))
        return result

    def positions(self) -> dict[str, int]:
        self._assert_enabled()
        try:
            response = self.session.get(
                f"{DHAN_API}/positions",
                headers={"access-token": self._access_token()}, timeout=20)
        except requests.RequestException as exc:
            raise LiveExecutionBlocked(f"could not fetch positions: {exc}") from exc
        if response.status_code >= 400:
            raise LiveExecutionBlocked(f"positions returned HTTP {response.status_code}")
        payload = _safe_json(response)
        rows = payload if isinstance(payload, list) else payload.get("data", [])
        return {r["securityId"]: int(r.get("netQty", 0)) for r in rows
                if r.get("securityId")}

    def _access_token(self) -> str:
        if self._token_provider is not None:
            return self._token_provider()
        from src.auth.dhan_token import DhanTokenManager

        return DhanTokenManager(self.config).get_token().access_token


def _safe_json(response: requests.Response) -> Any:
    try:
        return response.json()
    except ValueError:
        return {}
