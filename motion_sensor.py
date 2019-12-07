from gpiozero import LED
from gpiozero import MotionSensor

PIRPIN = 4
LEDPIN = 17

pir = MotionSensor(PIRPIN)
led = LED(LEDPIN)

led.off()

while True:
	pir.wait_for_motion()
	led.on()
	pir.wait_for_no_motion()
	led.off()