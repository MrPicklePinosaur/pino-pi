#Use temp/humidity sensor and ultrasonic sensor to measure distance (speed of sound is dependent on temp)

import RPi.GPIO as GPIO
import Adafruit_DHT as DHT
import time

GPIO.setmode(GPIO.BCM)

TRIGPIN = 4
ECHOPIN = 18
DHTPIN = 17

GPIO.setup(TRIGPIN,GPIO.OUT)
GPIO.setup(ECHOPIN,GPIO.IN)
GPIO.setup(DHTPIN,GPIO.IN)

#Get temp
DHT_SENSOR = DHT.DHT11
hum, temp = DHT.read(DHT_SENSOR,DHTPIN)
if hum is None or temp is None:
	print("DHT sensor error")
	exit()

print("Temp: "+str(temp)+" C Hum:"+str(hum))

#Ultrasonic
#send a quick ultrasonic burst
GPIO.output(TRIGPIN, True)
time.sleep(0.0001)
GPIO.output(TRIGPIN, False)

while GPIO.input(ECHOPIN) == False:
	start = time.time()

while GPIO.input(ECHOPIN) == True:
	end = time.time()

delta_time = end-start

#given the speed of sound, we know how long it took sound wave to reach target and back, so we can calculate distance to target
distance = (331 + 0.6*temp)*(delta_time/2)*100 # in cm, divided by two as the time recieved is the time for sound to get there AND baack

print('Distance: ' + str(distance) + ' cm')

GPIO.cleanup()