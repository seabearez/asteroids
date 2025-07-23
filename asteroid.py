from circleshape import *
from constants import *
import pygame
import random

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.position.x, self.position.y), self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
                
        random_angle = random.uniform(20,50)

        new_velocity_child_one = self.velocity.rotate(random_angle)
        new_velocity_child_two = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child_one = Asteroid(self.position.x, self.position.y, new_radius)
        child_two = Asteroid(self.position.x, self.position.y, new_radius)
        child_one.velocity = new_velocity_child_one * 1.2
        child_two.velocity = new_velocity_child_two * 1.2
