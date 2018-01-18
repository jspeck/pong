#	Johnathan Speck

import pygame

class ball:
    def __init__(self, x, y):
	    self.x = x
	    self.y = y
	    self.radius = 12
	    self.width = 0
	    self.generate_rect()

    def move(self, dx, dy):
	    self.x = self.x + dx
	    self.y = self.y + dy
	    self.generate_rect()

    def generate_rect(self):
	    self.rect = pygame.Rect(  self.x - self.radius, self.y - self.radius, self.radius + self.radius, self.radius + self.radius  )