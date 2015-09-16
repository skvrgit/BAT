
@ECHO OFF
setlocal enabledelayedexpansion

CALL  C:\Users\kanno\Desktop\BAT\Template\env.bat

IF "%~1"=="" (
  GOTO ARGERR
)

SET TODAY=%date:~-10,4%%date:~-5,2%%date:~-2,2%
IF %LOGFILE%.==. SET LOGFILE=%WLOGDIR%\%~n0_%TODAY%.log

IF NOT EXIST %LOGFILE%  GOTO FIRST
ECHO >>  [!DATE:~0,10! !TIME:~0,8!] 起動処理を開始
ECHO. >> LOGFILE


:FIRST 
ECHO  [!DATE:~0,10! !TIME:~0,8!] 処理を開始します。 >> %LOGFILE%

REM メイン処理



:ARGERR
ECHO [!DATE:~0,10! !TIME:~0,8!] 引数エラー 
EXIT /B 0

:END 
ECHO [!DATE:~0,10! !TIME:~0,8!] 処理が完了しました
EXIT /B 0

GOTO :EOF