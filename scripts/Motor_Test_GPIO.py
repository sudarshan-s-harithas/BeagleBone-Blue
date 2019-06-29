
#########Author - Sudarshan ###########
#######File Name - Motor_Test_beaglebone.py (tested for beagle bone Black)#########

import Adafruit_BBIO.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
 
Motor1A = P9_14
Motor1B = P9_13
Motor1E = P9_12
Motor2A = P9_11
Motor2B = P9_10
Motor2E = P9_9

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

left = GPIO.PWM(Motor1E, 100)
right = GPIO.PWM(Motor2E, 100)
left.start(25)
right.start(25)
 
print "Turning motor on"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
left.ChangeDutyCycle(100)
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
right.ChangeDutyCycle(100)
 
sleep(20)

left.stop()
right.stop()
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
 
GPIO.cleanup()


