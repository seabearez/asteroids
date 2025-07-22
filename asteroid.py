from circleshape import *
from constants import *
import pygame

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x,y)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.position.x, self.position.y), self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt