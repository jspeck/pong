#	Johnathan Speck

import pygame

class paddle:
    def __init__(self, x, y, w, h):
	    self.x = x
	    self.y = y
	    self.w = w 
	    self.h = h
	    self.rect = pygame.Rect(x, y, w, h)
	    self.score = 0

    def move(self, dy):
	    self.y = self.y + dy
	    self.rect = pygame.Rect(self.x, self.y, self.w, self.h)