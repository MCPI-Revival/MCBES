@ECHO OFF
TITLE MCBES PROXY
cd /d %~dp0

if exist src\MCBES.py (
  set MCBES_FILE=src\MCBES.py
) else (
  echo MCBES not found
  echo Downloads can be found at https://github.com/mcbes/mcbes/releases
  pause
  exit 1
)

python %MCBES_FILE% %* || pause
