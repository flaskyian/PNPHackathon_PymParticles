import RPi.GPIO as GPIO
from flask import Flask, render_template, request, redirect, url_for
app = Flask (__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledRed = 11
ledYellow = 13
ledWhite = 15
buzzer = 7

GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledYellow, GPIO.OUT)
GPIO.setup(ledWhite, GPIO.OUT)

GPIO.setup(buzzer, GPIO.OUT)


GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledYellow, GPIO.LOW)
GPIO.output(ledWhite, GPIO.LOW)

GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledYellow, GPIO.LOW)
GPIO.output(ledWhite, GPIO.LOW)

GPIO.output(buzzer, GPIO.LOW)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<deviceName>/<action>',methods=['POST'])
def operate(deviceName, action):
    if deviceName == "ledRed":
        actuator = ledRed
    if deviceName == "ledYellow":
        actuator = ledYellow
    if deviceName == "ledWhite":
        actuator = ledWhite
    if deviceName == "buzzer":
        actuator = buzzer
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
    

    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)

