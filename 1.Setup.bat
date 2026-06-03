@echo off
chcp 65001 >nul
title Cài dat va Khoi dong Super Studio
color 0A

echo =========================================================
echo      HETHONG TU DONG CAI DAT - SUPER STUDIO V37
echo =========================================================
echo.

echo [1/3] Dang kiem tra va cap nhat PIP...
python -m pip install --upgrade pip

echo. [1.5/3] cài đặt ffmpeg
winget install ffmpeg

echo.
echo [2/3] Dang tai va cai dat cac Module co ban (Gradio, TTS, Xu ly anh/am thanh)...
pip install gradio numpy soundfile edge-tts requests librosa deep-translator Pillow

echo.
echo [3/3] Dang cai dat Nao bo AI Whisper va Pytorch (Buoc nay co the mat vai phut neu chua co)...
pip install openai-whisper torch torchvision torchaudio

echo.
echo =========================================================
echo        CAI DAT HOAN TAT! DANG KICH HOAT TOOL...
echo =========================================================
echo.

python app.py

pause