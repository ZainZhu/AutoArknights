@ECHO OFF

for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"

SET timeStamp=%dt:~0,4%-%dt:~4,2%-%dt:~6,2%_%dt:~8,2%-%dt:~10,2%-%dt:~12,2%

SET mutID=_mut

@ECHO ON

adb -s 127.0.0.1:21503 shell logcat -v time > .\"%mutID%_%timeStamp%_logcat.log"

pause