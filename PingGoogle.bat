@echo off
setlocal

:PingLoop
ping -n 1 google.com | find "Ping request could not find host" > nul
if errorlevel 1 (
    echo Ping successful at %time%. Waiting for 1 minute.
    timeout /nobreak /t 60 > nul
    goto PingLoop
) else (
    echo Unable to ping. Waiting for 15 seconds.
    timeout /nobreak /t 15 > nul
    goto PingLoop
)

:end
echo Connection resumed. Exiting script.
endlocal