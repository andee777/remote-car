# Remote-car
![image](https://user-images.githubusercontent.com/29150454/114994291-a1034480-9e6a-11eb-90f2-3c23d90906c8.png)

## Pinout Pi Zero
<img src="https://user-images.githubusercontent.com/29150454/141723518-55242322-d2be-4f0b-a3c1-ca24f6866e59.png" width="400">

![image](https://user-images.githubusercontent.com/29150454/141728744-a68449b6-0285-45eb-9ac4-88515e193ecb.png)

### What do these numbers mean?
GPIO - General Purpose Input/Output, aka "BCM" or "Broadcom". These are the big numbers, e.g. "GPIO 22". You'll use these with RPi.GPIO and GPIO Zero.

Physical - or "Board" correspond to the pin's physical location on the header. These are the small numbers next to the header, e.g. "Physical Pin 15".

## Pi ssh accès
Utilisateur :   pi<br/>
Mot de passe :  andee


## Dépendences : 
- from flask import Flask, render_template, Response
- from flask_socketio import SocketIO
- import json
- import serial
- import adafruit_dht
- import board
- import busio
- import adafruit_pca9685
- from datetime import datetime, date
- import time
- from adafruit_servokit import ServoKit

