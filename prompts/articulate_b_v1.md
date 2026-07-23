SYNTH_V2 · Call B — Articulate (v1)

Call A classified this packet INVESTIGATE. Your job is to phrase, for a
practitioner, the QUESTION the divergence poses and the FALSIFIER that would
kill it. You are writing a lead to investigate — NOT a thesis, NOT a trade.

Output EXACTLY one JSON object, no prose around it:

  {"headline": "<one line framing the divergence>",
   "question": "<the one thing a human must resolve>",
   "falsifier": "<the specific observation that would kill this lead>",
   "cited_fields": [<dotted packet field paths you used, from CITABLE FIELDS>]}

Hard rules (enforced in code — violating any of these voids your output and the
reader gets the packet's own question and falsifier instead, so you add nothing
by breaking them):

1. USE ONLY THE PACKET. Every fact in every field you emit must correspond to a
   path in CITABLE FIELDS and appear in cited_fields. Do NOT introduce a
   mechanism, a cause, a catalyst detail, or a number that is not already in the
   packet. Articulation is phrasing, not supplementation. This is the highest
   risk in your task: a rich news cluster invites a tidy causal story — do not
   write one the packet doesn't contain.

2. NO VERDICT LANGUAGE. Never write "setup", "should", a probability, a percent,
   "likely to", or anything that asserts the lead will resolve. You frame a
   question; you do not answer it.

3. CHECKABLE FALSIFIER OR NOTHING. The falsifier must name a SPECIFIC observable
   condition tied to a packet field that a human could check — a level, a
   counter-move, a staleness test, a resolution within a stated window. A vague
   falsifier ("killed if it proves wrong") is void. If you cannot state a
   checkable falsifier, the packet's own falsifier is already good — yours is
   only used if it is better AND checkable.

PACKET:
{packet_json}

CITABLE FIELDS (you may cite only these paths):
{citable_fields}
