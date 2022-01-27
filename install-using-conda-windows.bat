@ECHO OFF
:: if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit )
call C:\ProgramData\Anaconda3\Scripts\activate
cd /d "%~dp0"
call conda config --append channels conda-forge
call conda env create -f environment.yml
echo Installed the environment successfully!
pause
:: FOR /F "delims=~" %f in (requirements.txt) DO conda install --yes "%f" || pip install "%f"