@echo off
color 03
echo Welcome to PEC Academic Analysis Software
ping -n 2 127.0.0.1>nul

echo Please make sure your computer is connected to the internet. If not, connect it and then launch this file. If connected already, please ignore !

ping -n 2 127.0.0.1>nul

echo Relax while we install the dependencies (Required only for the 1st time)

ping -n 2 127.0.0.1>nul
echo 5
ping -n 2 127.0.0.1>nul
echo 4
ping -n 2 127.0.0.1>nul
echo 3
ping -n 2 127.0.0.1>nul
echo 2
ping -n 2 127.0.0.1>nul
echo 1
ping -n 2 127.0.0.1>nul

echo Let's begin !
echo Installing Python 3.6.5 Silently
python-3.6.5-amd64.exe /quiet PrependPath=1 Include_launcher=0
echo Installing pip
python get-pip.py
echo Installing pandas
pip install pandas-0.24.1-cp36-cp36m-win_amd64.whl
echo Installing numpy
pip install numpy-1.16.1-cp36-cp36m-win_amd64.whl
echo Installing matplotlib
pip install matplotlib-3.0.2-cp36-cp36m-win_amd64.whl
echo Installing Pillow-PIL
pip install Pillow-5.4.1-cp36-cp36m-win_amd64.whl
echo Installing xlrd
pip install xlrd-1.2.0-py2.py3-none-any.whl


cls
echo Your Software is ready!
PAUSE
