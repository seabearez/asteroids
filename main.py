from constants import *
from player import *
import pygame

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 3, 0)
    dt = 0
    while True:
        BLACK = (0,0,0)
        # allows closing of program by exiting window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # colors background black
        screen.fill(BLACK)
        # draws player object
        player.draw(screen)
        # updates the full display surface to the screen. Objects drawn in the background then 'flipped' to surface 
        # to prevent tearing etc
        pygame.display.flip()
        dt = Clock.tick(60) / 1000


if __name__ == "__main__":
    main()
