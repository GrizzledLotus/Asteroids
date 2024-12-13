import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        frag1_velocity = self.velocity.rotate(random_angle)
        frag2_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        frag1 = Asteroid(self.position.x, self.position.y, new_radius)
        frag1.velocity = frag1_velocity * 1.2
        frag2 = Asteroid(self.position.x, self.position.y, new_radius)
        frag2.velocity = frag2_velocity * 1.2
