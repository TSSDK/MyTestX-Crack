
@echo off
set /p INPUT="Введи имя входного файла (например, game.exe): "
set /p OUTPUT="Введи имя выходного файла (или нажми Enter для Cracked.exe): "

if "%OUTPUT%"=="" set "OUTPUT=Cracked.exe"

if not exist "%INPUT%" (
    echo Ошибка: файл "%INPUT%" не найден.
    pause
    exit /b 1
)

.\script_mtx "%INPUT%" "%OUTPUT%"
echo Готово: %OUTPUT%
pause