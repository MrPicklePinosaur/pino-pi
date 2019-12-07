import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIRPIN = 4
LEDPIN = 17

GPIO.setup(LEDPIN,GPIO.OUT)
GPIO.setup(PIRPIN,GPIO.IN)

try:
	while True:
		time.sleep(0.1)

		state = GPIO.input(pir_sensor)
		if state == 1: #if motion is detected
			GPIO.output(LEDPIN,True)
		else:
			GPIO.output(LEDPIN,False)

except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
