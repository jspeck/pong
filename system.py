#	Johnathan Speck

import os
import pygame
from game import game
from key import key
from menu import menu

class system:
    def __init__(self):
	    self.SCREEN_SIZE = (640, 480)
	    self.FULLSCREEN = 0 
	    pygame.init()
	    pygame.mixer.init()

	    pygame.display.set_icon(pygame.image.load(os.path.join('img', 'pong_icon.png')))

	    self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
	    self.done = False
	    self.keys = []
	    self.fps = 60
	    self.clock = pygame.time.Clock()
	    self.tick = 0

	    self.caption = 'Pong'
	    pygame.display.set_caption(self.caption, 'Pong')

	    self.state = 1
	    self.statelist = []
	    self.statelist.append(game(self.SCREEN_SIZE))
	    self.statelist.append(menu(self.SCREEN_SIZE))
	
    def main_loop(self):
	    while not self.done:
		    self.screen.fill((0,0,0))
		    self.event_loop()
		    self.update()
		    self.draw()
		    self.play_sound()
		    pygame.display.flip()
		    self.clock.tick(self.fps)
		    self.tick = self.tick + 1

    def event_loop(self):
	    ev = pygame.event.get()
	    for event in ev:
		    if event.type == pygame.QUIT:
			    self.done = True
	    self.update_keyboard_input(ev)

    def update(self):
	    n = self.statelist[self.state].update(self.keys) 
	    if n == 0 and self.state == 1:
		    self.state = 0
	    elif n == 1:
		    self.done = True

    def draw(self):
	    self.screen.blit(self.statelist[self.state].draw(), (0, 0))

    def play_sound(self):
	    self.statelist[self.state].play_sound()

    def update_keyboard_input(self, ev):
	    just_pressed = []
	    just_released = []
	    del self.keys[:]

	    for event in ev:
		    if event.type == pygame.KEYDOWN:
			    if event.key not in just_pressed:
			        just_pressed.append(event.key)
			    elif event.key in just_pressed:
				    just_pressed.remove(event.key)
		    if event.type == pygame.KEYUP:
			    if event.key not in just_released:    
				    just_released.append(event.key)
			    elif event.key in just_released:
				    just_released.remove(event.key)

	    id = 0 
	    for k in pygame.key.get_pressed():
		    temp = key(id, (k == True), (id in just_pressed), (id in just_released))
		    self.keys.append(temp)
		    id = id + 1   

