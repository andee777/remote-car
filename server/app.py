#Import necessary libraries
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
# from datetime import datetime, date
import serial
# import json
# import time


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

# send to serial
@socketio.on('send')
def handle_send(data):
    # data = json.loads(json_str)
    print(data['message'])
    ser.write(data['message'].encode())
    # time.sleep(0.2)
    # print("sending to serial: %s"%data['message'])


if __name__ == '__main__':
    # Warning!!!
    # this must use `debug=False`
    # if you use `debug=True`,it will open serial twice, it will open serial failed!!!
    socketio.run(app, debug=False, host='0.0.0.0', port=5005)
