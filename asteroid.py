import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        a1 = Asteroid(
            self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS
        )
        a2 = Asteroid(
            self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS
        )
        a1.velocity = self.velocity.rotate(angle) * 1.2
        a2.velocity = self.velocity.rotate(-angle) * 1.2
