from flask import Flask, render_template, request, redirect, url_for, make_response
import RPi.GPIO as GPIO
import motors
import socket
from powertrain import Powertrain

direction_pins = (27, 23, 19, 20)
step_pins = (22, 24, 26, 21)
GPIO.setmode(GPIO.BOARD)

dexter = Powertrain(direction_pins, step_pins)
dexter.setup()

speed = 80
distance = 0.1

# Get server ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', server_ip=server_ip)


@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin)

    if changePin == 1:
        dexter.go('left', distance, speed, 0.05)
    elif changePin == 2:
        dexter.go('forward', distance, speed, 0.05)
    elif changePin == 3:
        dexter.go('right', distance, speed, 0.05)
    elif changePin == 4:
        dexter.go('backward', distance, speed, 0.05)
    elif changePin == 5:
        dexter.stop()
    else:
        print("Wrong command")

    response = make_response(redirect(url_for('index')))
    return (response)


app.run(debug=True, host='0.0.0.0', port=8000)
