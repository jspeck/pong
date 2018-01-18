#	Johnathan Speck

import os
import pygame
from key import key 

class menu:
    def __init__(self, SCREEN_SIZE):
	    self.SCREEN_SIZE = SCREEN_SIZE
	    self.buffer = pygame.Surface(self.SCREEN_SIZE)
	    self.state = 0 
	    self.font = pygame.font.SysFont("monospace", 36)
	    self.font2 = pygame.font.SysFont("monospace", 18)
	    self.text1 = textbox(175, 150, 300, 50, "Play", self.font)
	    self.text2 = textbox(175, 215, 300, 50, "Quit", self.font)
	    self.text3 = textbox(125, 300, 400, 50, "Red Controls: W/S $ Blue Controls: UP/DOWN", self.font2)
	    self.pos1 = (173, 147, 305, 55)
	    self.pos2 = (173, 212, 305, 55)
	    self.outer1 = outerbox(self.pos1)

    def update(self, keys):
	    self.keys = keys

	    if self.keys[pygame.K_RETURN].just_pressed == True:
		    return self.state

	    if self.keys[pygame.K_ESCAPE].just_pressed == True:
		    return 1 

	    if self.keys[pygame.K_UP].just_pressed == True:
		    self.state = self.state - 1
	    elif self.keys[pygame.K_DOWN].just_pressed == True:
		    self.state = self.state + 1

	    if self.state == 2:
		    self.state = 0
	    elif self.state == -1:
		    self.state = 1 

	    if self.state == 0:
		    self.outer1.change_pos(self.pos1)
	    elif self.state == 1:
		    self.outer1.change_pos(self.pos2)

	    return 2 

    def draw(self):
	    self.buffer.fill((0,0,0))
	    self.buffer.blit( self.outer1.get_draw_data(), (self.outer1.x, self.outer1.y) )
	    self.buffer.blit(self.text1.get_draw_data(), (self.text1.x, self.text1.y)) 
	    self.buffer.blit(self.text2.get_draw_data(), (self.text2.x, self.text2.y)) 
	    self.buffer.blit(self.text3.get_draw_data2(), (self.text3.x, self.text3.y)) 
	    return self.buffer

    def play_sound(self):
	    pass


class textbox:
    def __init__(self, x, y, w, h, string, font):
	    self.x = x
	    self.y = y
	    self.w = w
	    self.h = h 
	    self.string = string
	    self.rect = pygame.Rect(x, y, w, h)
	    self.font = font 

    def get_draw_data(self):
	    buffer = pygame.Surface((self.w, self.h))
	    pygame.draw.rect(buffer, (190,190,190), pygame.Rect(0, 0, self.w, self.h))
	    string = self.font.render(self.string, True, (250, 0, 0))
	    buffer.blit(string, ((self.w/3),(self.h/5))   )
	    return buffer 

    def get_draw_data2(self):
	    tstring = self.string.split("$")
	    buffer = pygame.Surface((self.w, self.h))
	    pygame.draw.rect(buffer, (190,190,190), pygame.Rect(0, 0, self.w, self.h))

	    string = self.font.render(tstring[0], True, (250, 0, 0))
	    buffer.blit(string, ((self.w/5)+10,(self.h/20)+3)   )

	    string = self.font.render(tstring[1], True, (0, 0, 250))
	    buffer.blit(string, ((self.w/7),(self.h/20)+20))

	    return buffer 

class outerbox:
    def __init__(self, pos):
	    self.x = pos[0]
	    self.y = pos[1]
	    self.w = pos[2]
	    self.h = pos[3]
	    self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def change_pos(self, pos):
	    self.x = pos[0]
	    self.y = pos[1]
	    self.w = pos[2]
	    self.h = pos[3]
	    self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def get_draw_data(self):
	    buffer = pygame.Surface((self.w, self.h))
	    pygame.draw.rect(buffer, (250, 0, 0), pygame.Rect(0, 0, self.w, self.h), 3)
	    return buffer 
	    