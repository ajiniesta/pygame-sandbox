import sys, pygame
from pygame.locals import *
from sdb_utils import *


class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/ball.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]
    
    def update(self, time, human_player, cpu_player, points):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time

        if self.rect.left <= 0:
            points[1] += 1
        if self.rect.right >= WIDTH:
            points[0] += 1

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
    
        if pygame.sprite.collide_rect(self, human_player):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        
        if pygame.sprite.collide_rect(self, cpu_player):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        
        return points


class Pala(pygame.sprite.Sprite):
    def __init__(self, x, keys_player=(K_UP, K_DOWN)):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.5
        self.keys_player = keys_player
    
    def move(self, time, keys):
        if self.rect.top >= 0:
            if keys[self.keys_player[0]]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[self.keys_player[1]]:
                self.rect.centery += self.speed * time

    def ia(self, time, ball):
        if ball.speed[0] >= 0 and ball.rect.centerx >= WIDTH/2:
            if self.rect.centery < ball.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self.speed * time
    
    def ia_left(self, time, ball):
        if ball.speed[0] <= 0 and ball.rect.centerx <= WIDTH/2:
            if self.rect.centery < ball.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self.speed * time
