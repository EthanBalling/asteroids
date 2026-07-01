import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        # Check if asteroid was small
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Calculate variables for splitting
        random_angle = random.uniform(20, 50)
        split1_vector = self.velocity.rotate(random_angle)
        split2_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = split1_vector * 1.2
        asteroid2.velocity = split2_vector * 1.2
        
        
        