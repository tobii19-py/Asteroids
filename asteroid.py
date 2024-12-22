from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        vec_1 = self.velocity.rotate(random_angle) * 1.2
        vec_2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        half_1 = Asteroid(self.position.x, self.position.y, new_radius)
        half_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        half_1.velocity = vec_1
        half_2.velocity = vec_2