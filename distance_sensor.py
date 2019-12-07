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

DHT_SENSOR = DHT.DHT11
hum, temp = DHT.read(DHT_SENSOR,DHTPIN)
if hum is not None and temp is not None:
	print("Temp: "+str(temp)+" C Hum:"+str(hum))
else
	print("Sensor error")

#send a quick ultrasonic burst
'''
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
'''
GPIO.cleanup()