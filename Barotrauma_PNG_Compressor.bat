@echo off

set "folder=%localappdata%\Daedalic Entertainment GmbH\Barotrauma\WorkshopMods\Installed"
set "path=%~dp0"

:start

for /R "%folder%" %%F in (*.png) do (
    "%path%pngquant.exe" --force --ext=.png --verbose --ordered --speed=1 --quality=50-90 "%%F"
)

shift
if not x%1==x goto start
