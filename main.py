from constants import *
import pygame
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
import sys, time

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    font = pygame.font.Font(None, 36)
    text_surface = font.render("Game Over!", True, "white")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        for obj in asteroids:
            if player.collide(obj):
                screen.blit(text_surface, (640, 360))
                pygame.display.flip()
                time.sleep(2)
                sys.exit()


if __name__ == "__main__":
    main()