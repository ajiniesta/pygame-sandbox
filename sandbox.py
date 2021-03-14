import sys, pygame
from pygame.locals import *
from sdb_utils import *
from sdb_sprites import Bola, Pala

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame sandbox")

    background_image = load_image('images/fondo_pong.png')
    bola = Bola()
    human_player = Pala(30, keys_player=(K_UP, K_DOWN))
    cpu_player = Pala(WIDTH - 30)
    clock = pygame.time.Clock()
    points = [0, 0]

    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)

        points = bola.update(time, human_player, cpu_player, points)
        human_player.move(time, keys)
        #human_player.ia_left(time, bola)
        cpu_player.ia(time, bola)

        p_1, p_1_rect = draw_text(str(points[0]), WIDTH/4, 40)
        p_2, p_2_rect = draw_text(str(points[1]), WIDTH-WIDTH/4, 40)

        screen.blit(background_image, (0, 0))
        screen.blit(p_1, p_1_rect)
        screen.blit(p_2, p_2_rect)
        screen.blit(bola.image, bola.rect)
        screen.blit(human_player.image, human_player.rect)
        screen.blit(cpu_player.image, cpu_player.rect)
        pygame.display.flip()
    return None

if __name__ == '__main__':
    pygame.init()
    main()