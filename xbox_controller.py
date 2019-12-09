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
		'''
		for evt in pygame.event.get():
			
			if evt.type == pygame.JOYAXISMOTION:
                            print("YEEET")
        '''

        for j in joysticks:

        	for axis in range(j.get_numaxes()):
        		print("Axis #"+axis+": "+j.get_axis(axis)) 

        	for ball in range(j.get_numballs()):
        		print("Ball #"+ball+": "+j.get_ball(ball)) 

        	for button in range(j.get_numbuttons()):
        		print("Button #"+button+": "+j.get_button(button)) 

        	for hat in range(j.get_numhats()):
        		print("Hat #"+hat+": "+j.get_hat(hat)) 

        	print("=-=-=-=-=-=-=-=-=")

except KeyboardInterrupt:
	pass
finally:
	pygame.quit()