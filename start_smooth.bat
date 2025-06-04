@echo off
python open_audio.py

if %errorlevel% equ 0 (
    echo open_audio.py ended successfully. main.py will be started.
    python main.py --smooth
) else (
    echo open_audio.py ended with an error. main.py will not be started.
    pause
)