@echo off
chcp 65001 >nul 2>&1
echo ========================================
echo   漢文 텍스트 교감기 설치 및 실행
echo ========================================
echo.

:: Python 확인
python --version >nul 2>&1
if errorlevel 1 (
    echo [오류] Python이 설치되어 있지 않습니다.
    echo https://www.python.org/downloads/ 에서 Python을 설치하세요.
    echo 설치 시 "Add Python to PATH" 체크를 잊지 마세요!
    pause
    exit /b 1
)

:: pywebview 설치
echo [1/2] pywebview 패키지 설치 중...
pip install pywebview >nul 2>&1
if errorlevel 1 (
    echo pip install 실패. 수동으로 실행하세요: pip install pywebview
    pause
    exit /b 1
)
echo      설치 완료!
echo.

:: 실행
echo [2/2] 교감기를 실행합니다...
python "%~dp0run.py"
