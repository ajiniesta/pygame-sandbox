import sys, pygame
from pygame.locals import *


WIDTH = 640
HEIGHT = 480

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error:
                raise SystemExit
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

def draw_text(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font("fonts/DroidSans.ttf", 25)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect