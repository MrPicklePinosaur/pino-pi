import RPi.GPIO as GPIO
import time

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

#main stuff
GPIO.output(18,GPIO.HIGH)
time.sleep(5)
GPIO.output(18,GPIO.LOW)
GPIO.cleanup()