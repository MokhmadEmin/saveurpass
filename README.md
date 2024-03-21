![alt text](https://github.com/MokhmadEmin/saveurpass/blob/main/img_md/logo.png?raw=true)
<h1><b>SaveUrPass</b> - it is a command, local, safe and open password manager.</h1>
You can save all your passwords on your computer, knowing only one
<h3>How to install:</h3>
At first, you need install programming language "Python".<br>
Linux:
```
sudo [package manager name] install python3
```
Then you have to download the repository using Git.
```
sudo [package manager name] apt-get install git
```
```
git clone https://github.com/MokhmadEmin/saveurpass.git
```
Go to the repository source and download the virtual environment.
```
cd saveurpass
```
```
sudo [package manager name] install python3-venv
```
```
python3 -m venv venv
```
We go into the virtual environment and download libraries via pip.<br>
```
. venv/bin/activate
```
```
pip3 install -r requirements.txt
```
And Start app!
```
python3 main.py
```
![alt text](https://github.com/MokhmadEmin/saveurpass/blob/main/img_md/screenshot.JPG?raw=true)
