@echo off
setlocal

:: Check if venv exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error creating virtual environment. Exiting.
        exit /b 1
    )
) else (
    echo Virtual environment already exists. Skipping creation.
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo Error activating virtual environment. Exiting.
    exit /b 1
)

:: Install Pillow
echo Installing Pillow...
pip install pillow
if errorlevel 1 (
    echo Error installing Pillow. Exiting.
    exit /b 1
)

:: Run the Python script
echo Running convert.py...
python convert.py
if errorlevel 1 (
    echo Error running convert.py. Exiting.
    exit /b 1
)

:: Keep the command window open
pause
