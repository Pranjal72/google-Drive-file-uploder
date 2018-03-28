# google-Drive-file-uploder

Simple script to convert a file into zip and upload zip file on Google Drive.

## Description
Script uses predefined [Drive APIs Client ID and Client Secret].
It takes upload file as command line argument, uploads it and sets permissions that anyone who has download link can download the file.

## Requirements
Python 2.7.4
pydrive(http://pythonhosted.org/PyDrive/quickstart.html) use this link for reference.
[google-api-python-client](http://code.google.com/p/google-api-python-client/)

## Configuration
use the link (https://console.developers.google.com/start/api?id=drive) to generate **client ID** and **client secret** strings (download `client_secret.json`). Choose **other** for **application type**.
save the `client_secret.json` and `quickstart.py` in the same folder.

## Procedure
Step1:Open the command prompt
Step2:Navigate to the folder path
Step3:Run the program (python quickstart.py)
Step4:Provide the folder path that has to be zipped and uploaded.

#Note:
=> This is my first Project on Python it is done under the guidance of Zaid Sir from Digipodium.
=> Made by Pranjal Shukla(prnjlshukla.98@gmail.com).
