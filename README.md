![alt text](https://github.com/MokhmadEmin/saveurpass/blob/main/img_md/logo.png?raw=true)
<h1><b>SaveUrPass</b> - it is a command, local, safe and open password manager.</h1>
You can save all your passwords on your computer, knowing only one
<h3>How to install:</h3>
At first, you need install programming language "Python".<br>
Linux:<br>
```bash
sudo [package manager name] install python3
```<br>
Then you have to download the repository using Git.<br>
```bash
sudo [package manager name] apt-get install git
```<br>
```bash
git clone https://github.com/MokhmadEmin/saveurpass.git
```
Go to the repository source and download the virtual environment.<br>
```bash
cd saveurpass
```<br>
```bash
sudo [package manager name] install python3-venv
```<br>
```bash
python3 -m venv venv
```<br>
We go into the virtual environment and download libraries via pip.<br>
```bash
. venv/bin/activate
```<br>
```bash
pip3 install -r requirements.txt
```
And Start app!<br>
```bash
python3 main.py
```
