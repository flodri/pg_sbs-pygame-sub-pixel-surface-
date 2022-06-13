import pygame
from pygame.locals import SRCALPHA
from subpixelsurface import SubPixelSurface
from math import sin, cos

NUM_BALLS = 100


def run():
    
    pygame.init()
    screen = pygame.display.set_mode((640, 480))  
    pygame.font.init()
    base_font = pygame.font.SysFont(None, size=32)
    clock = pygame.time.Clock()

    pingball = pygame.Surface((24, 24), flags=SRCALPHA)
    pingball.fill((192, 192, 69, 64))
    pygame.draw.circle(pingball, (192, 192, 192), (12, 12), 8)

    pingball_subpixel = SubPixelSurface(pingball, x_level=4)
    
    backgroung = pygame.Surface((640, 480))
    backgroung.fill((127, 3, 3))
    backgroung.blit(base_font.render('Without sub-pixel', True, (255, 255, 255)),
                    (80, 64)
                    )
    backgroung.blit(base_font.render('With sub-pixel', True, (255, 255, 255)),
                    (415, 64)
                    )

    t = 0
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        time_passed = clock.tick(60)
        t += time_passed / 4000

        screen.blit(backgroung, (0, 0))

        for n in range(NUM_BALLS):
            a = n / NUM_BALLS * 40
            x = sin((t + a) * 0.74534) * 100 + 160
            y = cos(((t * 1.232) + a) * 0.453464) * 100 + 240
                        
            screen.blit(pingball, (x, y))
            screen.blit(pingball_subpixel.at(x, y), (x+320, y))

        pygame.display.set_caption(f'{round(clock.get_fps())}')
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    run()
