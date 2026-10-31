@echo off
setlocal
echo ================================================================
echo   OptiCrop - Push to GitHub
echo   Repository: https://github.com/pithanibhaskarsivakumar-p/OptiCrop
echo ================================================================
echo.

set "PATH=C:\Users\hi\AppData\Local\Programs\Git\cmd;C:\Users\hi\AppData\Local\Programs\gh\bin;%PATH%"

echo Option 1: Press ENTER to authenticate via your browser
echo Option 2: Or paste your GitHub Personal Access Token (PAT) below
echo.
set /p TOKEN="Enter GitHub Token (or press ENTER to use browser login): "

if "%TOKEN%"=="" (
    echo.
    echo Launching browser authentication...
    gh auth login --web -h github.com -p https
    gh auth setup-git
    git push -u origin main
) else (
    echo.
    echo Pushing with provided token...
    git push https://%TOKEN%@github.com/pithanibhaskarsivakumar-p/OptiCrop.git main
)

echo.
echo ================================================================
echo Done! Check your repository at:
echo https://github.com/pithanibhaskarsivakumar-p/OptiCrop
echo ================================================================
echo.
pause
