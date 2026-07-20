@echo off
rem Giants & Gears — local viewer (optional; double-clicking index.html also works)
cd /d "%~dp0"
start "" http://localhost:8321/
py -3.11 -m http.server 8321
