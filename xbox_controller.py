import pygame
pygame.init()
pygame.display.init()
pygame.joystick.init()

joysticks = []
print(pygame.joystick.get_count())
for i in range(pygame.joystick.get_count()):
	joysticks.append(pygame.joystick.Joystick(i))
	joysticks[-1].init()

	print("Initializing joystick "+joysticks[-1].get_name())


try:
	while True:
		for evt in pygame.event.get():
			pass


except KeyboardInterrupt:
	pass
finally:
	pygame.quit()