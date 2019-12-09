import pygame
pygame.init()

joysticks = []
print(pygame.joystick.get_count())
for i in range(pygame.joystick.get_count()):
	joysticks.append(pygame.joystick.Joystick(i))
	joysticks[-1].init()

	print("Initializing joystick "+joystick[-1].get_name())

'''
try:
	while True:



except KeyboardInterrupt:
	pass
'''