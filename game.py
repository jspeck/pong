#	Johnathan Speck

import os
import pygame
from paddle import paddle 
from ball import ball
from key import key

class game:
    def __init__(self, SCREEN_SIZE):

	    self.SCREEN_SIZE = SCREEN_SIZE

	    self.buffer = pygame.Surface((640, 480))
	    pygame.mixer.init()
	    self.sound = []
	    self.sound.append( pygame.mixer.Sound(os.path.join('snd', 'ping_pong_8bit_beeep.ogg')) )
	    self.sound.append( pygame.mixer.Sound(os.path.join('snd', 'ping_pong_8bit_peeeeeep.ogg')) )
	    self.sound.append( pygame.mixer.Sound(os.path.join('snd', 'ping_pong_8bit_plop.ogg')) )
	    self.soundcount = 0

	    self.ball_speed = (-5, -5)
	    self.font = pygame.font.SysFont("monospace", 42)

	    self.paddle_speed = 4
	    self.p1 = paddle(20, 240, 10, 70)
	    self.p2 = paddle(610, 240, 10, 70)
	    self.ball = ball( 320 , 240 )
	    self.play = False
	    self.hit = False

	    self.keys = []

    def update(self, keys):
	    self.keys = keys

	    if self.keys[pygame.K_ESCAPE].just_pressed == True:
		    return 1 

	    if self.keys[pygame.K_w].down == True:
		    self.p1.move(-self.paddle_speed)
	    elif self.keys[pygame.K_s].down == True:
		    self.p1.move(self.paddle_speed)

	    if self.keys[pygame.K_UP].down == True:
		    self.p2.move(-self.paddle_speed)
	    elif self.keys[pygame.K_DOWN].down == True:
		    self.p2.move(self.paddle_speed)

	    if self.keys[pygame.K_SPACE].just_pressed == True:
		    self.play = True

	    if self.play == True:
		    self.ball.move( self.ball_speed[0], self.ball_speed[1]  )

	    if self.ball.y + self.ball.radius >= self.SCREEN_SIZE[1] or self.ball.y - self.ball.radius <= 0:
		    self.ball_speed = ( self.ball_speed[0], -self.ball_speed[1] )

	    if self.p1.rect.colliderect(self.ball.rect) and self.ball.x >= self.p1.rect.right:
		    self.ball_speed = ( -self.ball_speed[0], self.ball_speed[1] ) 
		    self.hit = True

	    if self.p2.rect.colliderect(self.ball.rect) and self.ball.x <= self.p2.rect.left:
		    self.ball_speed = ( -self.ball_speed[0], self.ball_speed[1] ) 
		    self.hit = True

	    if self.ball.x < 0:
		    self.p2.score = self.p2.score + 1
		    self.reset()
	    elif self.ball.x > self.SCREEN_SIZE[0]:
		    self.p1.score = self.p1.score + 1
		    self.reset()

	    return 2 

    def draw(self):
	    self.buffer.fill((0,0,0))
	    pygame.draw.rect(self.buffer, (250, 0, 0), self.p1.rect) 
	    pygame.draw.rect(self.buffer, (0, 0, 250), self.p2.rect) 
	    pygame.draw.circle(self.buffer, (250, 250, 250), (self.ball.x, self.ball.y), self.ball.radius, self.ball.width)
	    #pygame.draw.rect(self.screen, (255, 0, 255), self.ball.rect)
	    redscore = self.font.render(str(self.p1.score), True, (250, 0, 0))
	    bluescore = self.font.render(str(self.p2.score), True, (0, 0, 255))
	    self.buffer.blit(redscore, (70, 425))
	    self.buffer.blit(bluescore, (570, 425))
	    return self.buffer 

    def play_sound(self):
	    if self.hit == True:
		    self.sound[self.soundcount].play()
		    self.soundcount = self.soundcount + 1
		    self.hit = False
	    if self.soundcount == 3:
		    self.soundcount = 0

    def reset(self):
	    self.play = False
	    self.ball.x = 320
	    self.ball.y = 240