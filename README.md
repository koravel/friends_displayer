# What is this?
This is app that can extract names and page links of all your friends on facebook.
## Reqirements
* Python 3.7+
* Google Chrome browser 74
* Chrome Driver
* Selenium 3.141

## Installation
### Windows
1. Download and install Python 3.7+: https://www.python.org/downloads/
2. Download Chrome Driver: https://sites.google.com/a/chromium.org/chromedriver/downloads
3. Unzip `chromedriver_win32.zip` to `...<app_folder>/env/`  
4. Download and install Google Chrome: https://www.google.ru/chrome/
2. Change `driver_location` setting in settings.json to `./env/chromedriver.exe`
### Linux
1. Run install.sh
2. Change `driver_location` setting in settings.json to `/usr/bin/chromedriver`
## Launch
1. Edit `login` and `pass` settings to yours.
2. Run `run.bat`(Windows) or `run.sh`(Linux)

## Output example
```
'
---------------------------------
name:Kostya Panchenko
link:https://www.facebook.com/kostya.panchenko.127
---------------------------------
name:Дмитрий Солонцевой
link:https://www.facebook.com/profile.php?id=100035970048527
---------------------------------
name:Testeslav Testesnik
link:https://www.facebook.com/testeslav.testesnik.7
---------------------------------
name:Artem Sysa
link:https://www.facebook.com/artem.sysa.1
---------------------------------
name:Dmitry Shekhovtsov
link:https://www.facebook.com/dmitry.shekhovtsov25
---------------------------------
```
