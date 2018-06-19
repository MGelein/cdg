@echo off
setlocal enableDelayedExpansion

::Save the command output to a text file
python cdg.py %* > temp.txt

:: Determine number of lines, this is some kind of dark BATCH magic...
For /f %%j in ('Find "" /v /c ^<temp.txt') Do Set /a cnt=%%j

:: Check if there is only one result, if so, cd to it
If %cnt% EQU 1 (
    start temp.bat
) else (
    :: Read the file into an array
    <temp.txt (
        for /l %%N in (1 1 %cnt%) do (
            set "str.%%N="
            set /p "str.%%N="
        )
    )
    :: Display the array values
    for /l %%N in (1 1 %cnt%) do echo(!str.%%N!)
)
:: Remove temp file
del temp.txt