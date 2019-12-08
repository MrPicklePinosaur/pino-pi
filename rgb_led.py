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
		request = input()
		print(request)
		if (len(request) != 3):
			continue

		GPIO.output(REDPIN,request[0])
		GPIO.output(GREENPIN,request[1])
		GPIO.output(BLUEPIN,request[2])


except KeyboardInterrupt:
	GPIO.cleanup()