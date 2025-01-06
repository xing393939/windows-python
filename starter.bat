@echo off
echo starter.exe running
starter.exe

if %ERRORLEVEL% neq 0 (
    echo starter.exe error: %ERRORLEVEL%
) else (
    echo starter.exe ok
)

pause