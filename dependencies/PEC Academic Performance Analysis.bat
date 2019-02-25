@echo on
color 03
echo Welcome to PEC Academic Analysis Software
ping -n 2 127.0.0.1>nul
mail\Scripts\activate
python PEC_Performance_Analytics.py
PAUSE
