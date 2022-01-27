@ECHO OFF
call C:\ProgramData\Anaconda3\Scripts\activate
cd /d "%~dp0"
call conda activate mac
SET FLASK_APP=app.py
python -m flask run