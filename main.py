# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_fill_counter = 0
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    


    while screen_fill_counter >= 0:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  return

      updatable.update(dt)      

      for asteroid in asteroids:
            if player.collison(asteroid) == True:
                  print("Game over!")
                  sys.exit()
                  
            for bullet in shots:
                  if asteroid.collison(bullet) == True:
                       asteroid.split()
                       pygame.sprite.Sprite.kill(bullet)

      pygame.Surface.fill(screen, (0, 0, 0))
      for draw in drawable:
            draw.draw(screen)
        
      screen_fill_counter += 1

      pygame.display.flip()

      dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()