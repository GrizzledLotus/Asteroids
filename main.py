# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# print("Starting asteroids!")
# print(f"Screen width: {SCREEN_WIDTH}")
# print(f"Screen height: {SCREEN_HEIGHT}")

# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    # Initialize pygame when we actually start the game
    pygame.init()
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create game FPS
    game_clock = pygame.time.Clock()
     
    # Creating groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # print(f"Updatables: {len(updatables)}")
    # print(f"Drawables: {len(drawables)}")
    # print(f"Asteroids: {len(asteroids)}")

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)
        
    # Create instances
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    # print(f"Player groups: {player.groups()}")
    # print(f"Asteroid field groups: {asteroid_field.groups()}")

    dt = 0
    
    # Start game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # player.update(dt)
        # Update all updatable sprites
        for sprite in updatables:
            sprite.update(dt)
        
        for asteroid in asteroids:
            if player.is_colliding_with(asteroid):
                print("Game Over!")
                running = False

            for shot in shots:
                if asteroid.is_colliding_with(shot):
                    shot.kill()
                    asteroid.split()

        # Fill screen with black
        screen.fill("black")
    
        # Render player on screen
        # player.draw(screen)
        # Draw all drawable sprites
        for sprite in drawables:
            sprite.draw(screen)

        # Update display
        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()
