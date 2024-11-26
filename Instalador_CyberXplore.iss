[Setup]
AppName=CyberXplore
AppVersion=1.0
DefaultDirName={commonpf}\CyberXplore
DefaultGroupName=CyberXplore
OutputDir=Output
OutputBaseFilename=CyberXplore
UninstallDisplayIcon={app}\CyberXplore.exe
Uninstallable=yes
Compression=lzma
SolidCompression=yes

[Files]
; Copiar el ejecutable principal de la aplicación
Source: "dist\CyberXplore.exe"; DestDir: "{app}"; Flags: ignoreversion

; Copiar los iconos de la GUI
Source: "img\*"; DestDir: "{app}\img"; Flags: recursesubdirs createallsubdirs

; Copiar los archivos de la interfaz de Nmap
Source: "interfaces\GUINmap\*"; DestDir: "{app}\interfaces\GUINmap"; Flags: recursesubdirs createallsubdirs

; Copiar los archivos de la interfaz de Sherlock
Source: "interfaces\GUISherlock\*"; DestDir: "{app}\interfaces\GUISherlock"; Flags: recursesubdirs createallsubdirs

; Incluir Nmap (instalador) y Python (instalador) en la carpeta temporal para instalación posterior
Source: "nmap-7.94-setup.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall
Source: "python-3.13.0-amd64.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall

[Run]
; Verificar si Python está instalado
Filename: "cmd.exe"; Parameters: "/C python --version"; Flags: runhidden; Check: IsPythonInstalled; StatusMsg: "Verificando si Python está instalado..."

; Si Python no está instalado, instalarlo
Filename: "{tmp}\python-3.13.0-amd64.exe"; Parameters: "/quiet InstallAllUsers=1 PrependPath=1"; Flags: waituntilterminated; StatusMsg: "Instalando Python..."; Check: Not IsPythonInstalled

; Instalar Nmap
Filename: "{tmp}\nmap-7.94-setup.exe"; Flags: waituntilterminated; StatusMsg: "Instalando Nmap, sigue las instrucciones en pantalla..."

; Instalar dependencias de Sherlock desde requirements.txt
Filename: "cmd.exe"; Parameters: "/C python -m pip install -r {app}\interfaces\GUISherlock\sherlock-master\requirements.txt"; Flags: waituntilterminated; StatusMsg: "Instalando dependencias de Sherlock..."; Check: IsPythonInstalled

; Ejecutar la aplicación CyberXplore después de la instalación
Filename: "{app}\CyberXplore.exe"; Flags: nowait postinstall

[UninstallDelete]
; Eliminar archivos y carpetas durante la desinstalación
Type: files; Name: "{app}\interfaces\GUINmap\*"
Type: dirifempty; Name: "{app}\interfaces\GUINmap"
Type: files; Name: "{app}\interfaces\GUISherlock\*"
Type: dirifempty; Name: "{app}\interfaces\GUISherlock"
Type: files; Name: "{app}\CyberXplore.exe"
Type: dirifempty; Name: "{app}"

[Icons]
; Crear accesos directos en el escritorio y en el menú de inicio
Name: "{group}\CyberXplore"; Filename: "{app}\CyberXplore.exe"
Name: "{commondesktop}\CyberXplore"; Filename: "{app}\CyberXplore.exe"

[Code]
function IsPythonInstalled: Boolean;
begin
  Result := RegKeyExists(HKEY_LOCAL_MACHINE, 'SOFTWARE\Python\PythonCore\3');  // Verifica si Python está instalado en el registro
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usPostUninstall then
  begin
    DelTree(ExpandConstant('{app}'), True, True, True); // Elimina la carpeta principal
  end;
end;