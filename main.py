from asteroid import *
from asteroidfield import *
from constants import *
from player import *

import pygame

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 3, 0)
    asteroidfield = AsteroidField()
    dt = 0

    while True:
        # allows closing of program by exiting window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # colors background black
        screen.fill(BLACK)
        dt = Clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                return
        # draws each object in drawables group
        for pic in drawable:
            pic.draw(screen)
        # updates the full display surface to the screen. Objects drawn in the background then 'flipped' to surface 
        # to prevent tearing etc
        pygame.display.flip()


if __name__ == "__main__":
    main()
