# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from pygame.display import update

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    c = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    p = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    af = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for group in updatable:
            group.update(dt)
        for group in drawable:
            group.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(p):
                print("Game over!")
                sys.exit()


        pygame.display.flip()
        dt = (c.tick(60)) / 1000


if __name__ == "__main__":
    main()
