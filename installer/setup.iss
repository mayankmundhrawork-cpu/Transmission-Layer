; Inno Setup script for the PIT Factor Research Platform desktop build.
; Compiled by .github/workflows/desktop-build.yml on windows-latest.

#define AppName "PIT Factor Research Platform"
#define AppPublisher "Transmission Layer"
#define AppExeName "PITFactorPlatform.exe"
#ifndef AppVersion
  #define AppVersion "0.1.0"
#endif

[Setup]
AppId={{7C1B4E2A-9D3F-4A61-8B57-2E9A4C6D1F03}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
DefaultDirName={autopf}\PITFactorPlatform
DefaultGroupName={#AppName}
DisableProgramGroupPage=yes
OutputDir=Output
OutputBaseFilename=PITFactorPlatform-{#AppVersion}-setup
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
; Per-user install by default: no admin prompt, and the data directory the app
; writes to is under the user's profile anyway.
PrivilegesRequiredOverridesAllowed=dialog
ArchitecturesInstallIn64BitMode=x64compatible
UninstallDisplayName={#AppName}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"

[Files]
Source: "..\dist\PITFactorPlatform\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\{#AppExeName}"
Name: "{group}\Uninstall {#AppName}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\{#AppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#AppExeName}"; Description: "Launch {#AppName}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
; Remove only what the installer created. The user's archive and database live
; under %LOCALAPPDATA% and are deliberately NOT deleted — an uninstall must not
; destroy a multi-hour data backfill.
Type: filesandordirs; Name: "{app}\_internal"
