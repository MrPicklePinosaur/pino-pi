import pygame
pygame.init()
pygame.display.init()
pygame.joystick.init()

'''
joysticks = []
print(pygame.joystick.get_count())
for i in range(pygame.joystick.get_count()):
	joysticks.append(pygame.joystick.Joystick(i))
	joysticks[-1].init()

	print("Initializing joystick "+joysticks[-1].get_name())
'''

try:
	while True:

        for joy in range(pygame.joystick.get_count()):
        	j = pygame.joystick.JoyStick(joy)
        	j.init()

        	print(j.get_numaxes())
        	for axis in range(j.get_numaxes()):
        		print(f"Axis # {axis}: {j.get_axis(axis)}") 

        	for ball in range(j.get_numballs()):
        		print(f"Ball # {ball}: {j.get_ball(ball)}") 

        	for button in range(j.get_numbuttons()):
        		print(f"Button # {button}: {j.get_button(button)}") 

        	for hat in range(j.get_numhats()):
        		print(f"Hat # {hat}: {j.get_hat(hat)}") 

        	print("=-=-=-=-=-=-=-=-=")

except KeyboardInterrupt:
	pass
finally:
	print("quit or errored")
	pygame.quit()