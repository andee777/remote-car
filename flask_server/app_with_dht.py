#Import necessary libraries
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import json
import serial
import adafruit_dht
import board
import busio
import adafruit_pca9685
from datetime import datetime, date
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)


# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D16)

app = Flask(__name__)
app.static_folder = 'static'
socketio = SocketIO(app)
ser = serial.Serial("/dev/ttyUSB0", 9600)

# disable requests logging
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# index
@app.route('/')
def index():
    return render_template('index.html')


# get serial in background
def gen_serial():
    while True:
        cc=str(ser.readline())
        # print(cc[2:][:-5])
        socketio.emit("serial_message", data={"message": cc[2:][:-5]})
        
socketio.start_background_task(gen_serial)

# get dht in background
def gen_dht():
    while True:
        # time.sleep(5.0)
        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            cc=str(
                "Temp: {:.1f} C    Humidity: {}% ".format(
                    temperature_c, humidity
                )
            )
            now = datetime.now()
            today = date.today()
            # print("Date:", today)
            current_time = now.strftime("%H:%M:%S")
            # print("Time =", current_time)
            # print(cc)
            socketio.emit("dht_message", data={"message": cc, "time": str(current_time), "date": str(today)})
    
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            # print(error.args[0])
            # socketio.emit("dht_message", data={"message": error.args[0]})
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
    

        
        
socketio.start_background_task(gen_dht)

# send to serial
@socketio.on('send')
def handle_send(data):
    # data = json.loads(json_str)
    print(data['message'])
    ser.write(data['message'].encode())
    # time.sleep(0.2)
    # print("sending to serial: %s"%data['message'])

# send to serial
@socketio.on('cam')
def handle_cam(data):
    # data = json.loads(json_str)
    print(data['message'])
    kit.servo[2].angle = 90
    time.sleep(0.5)
    kit.servo[2].angle = 120

if __name__ == '__main__':
    # Warning!!!
    # this must use `debug=False`
    # if you use `debug=True`,it will open serial twice, it will open serial failed!!!
    socketio.run(app, debug=False, host='0.0.0.0', port=5005)
