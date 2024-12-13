# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import Player

print("Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    # Initialize pygame when we actually start the game
    pygame.init()
    
    # Create game FPS
    game_clock = pygame.time.Clock()
    dt = 0

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create player instance
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

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
