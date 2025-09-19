# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_fill_counter = 0
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    


    while screen_fill_counter >= 0:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        return
                
        pygame.Surface.fill(screen, (0, 0, 0))
        for draw in drawable:
              draw.draw(screen)
        updatable.update(dt)
        screen_fill_counter += 1
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()