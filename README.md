# Shazam-Like-App
A shazam-like app me and [@sudowicked](https://github.com/sudowicked) created for a university class.

A vital part of this project was [this](https://www.mathworks.com/matlabcentral/fileexchange/23332-robust-landmark-based-audio-fingerprinting) library.

A video demonstrating the app's functionality can be found [here](https://www.youtube.com/watch?v=w-dbCmugTGQ).

<br>

<img width="391" height="460" alt="image" src="https://github.com/user-attachments/assets/934267e7-7490-4d98-a33b-64236b8e82ed" />
<img width="391" height="460" alt="Screenshot from 2025-08-12 18-23-17" src="https://github.com/user-attachments/assets/3b52ef01-ff32-4108-939b-980e4fb80bf6" />
<p align="center">
  <img width="391" height="460" alt="Screenshot from 2025-08-12 18-23-38" src="https://github.com/user-attachments/assets/099c0725-a03e-40fb-b160-e295e46916da" />
</p>

<br>

## Installation Instructions (TESTED ON DEBIAN AND ARCH LINUX):

### 1) Install GNU Octave:<br>
$ ***sudo apt install octave***<br>
$ ***sudo apt install octave-dev***

### 2) Create a python virtual environment inside the Shazam-Like-app-master/app directory to install the necessary modules:<br>
$ ***python3 -m venv .venv***<br>
$ ***source .venv/bin/activate*** (always run this command when you want to execute the application)

### 3) Python modules installation:
$ ***sudo apt install python3-tk*** (tkinter)<br>
$ ***pip3 install oct2py*** (oct2py)<br>
$ ***pip3 install pillow*** (PIL)

### 4) Octave packages installation:
Open GNU Octave and inside the command window type:<br>
$ ***pkg install -forge io*** (if you get an error running 'make' for the io package run this command: $ ***sudo apt install build-essential***)<br>
$ ***pkg install -forge signal*** (if prompted to update the control package, run: $ ***pkg install -forge control*** and restart Octave)

### 5) Install necessary system MP3 libraries:
$ ***sudo apt install lame*** (LAME MP3 encoder)<br>
$ ***sudo apt install mp3info*** (MP3Info for data extraction)<br>
$ ***sudo apt install mpg123*** (MPG123 decoder)

### 6) Run Khazam
Inside the /app directory execute:<br>
$ ***python3 main.py***
