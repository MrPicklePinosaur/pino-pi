import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

REDPIN = 11
GREENPIN = 13
BLUEPIN = 15

GPIO.setup(REDPIN,GPIO.OUT)
GPIO.setup(GREENPIN,GPIO.OUT)
GPIO.setup(BLUEPIN,GPIO.OUT)

try:
	while True:
		request = str(input())

		if (len(request) != 3):
			continue

		GPIO.output(REDPIN,int(request[0]))
		GPIO.output(GREENPIN,int(request[1]))
		GPIO.output(BLUEPIN,int(request[2]))


except KeyboardInterrupt:
	GPIO.cleanup()