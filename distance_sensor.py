import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIGPIN = 4
ECHOPIN = 18

GPIO.setup(TRIGPIN,GPIO.OUT)
GPIO.setup(ECHOPIN,GPIO.IN)

#send a quick ultrasonic burst
GPIO.output(TRIGPIN, True)
time.sleep(0.0001)
GPIO.output(TRIGPIN, False)

while GPIO.input(ECHOPIN) == False:
	start = time.time()

while GPIO.input(ECHOPIN) == True:
	end = time.time()

delta_time = end-start

distance = delta_time/0.000058 #given the speed of sound, we know how long it took sound wave to reach target and back, so we can calculate distance to target

print('Distance: ' + str(distance) + ' cm')