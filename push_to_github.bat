@echo off
echo ======================================================
echo   Pushing OptiCrop to GitHub Profile:
echo   https://github.com/pithanibhaskarsivakumar-p/OptiCrop
echo ======================================================
echo.

set "PATH=C:\Users\hi\AppData\Local\Programs\Git\cmd;%PATH%"

git branch -M main
git remote set-url origin https://github.com/pithanibhaskarsivakumar-p/OptiCrop.git
git push -u origin main

echo.
pause
