# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *

print("Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    # Initialize pygame when we actually start the game
    pygame.init()
    
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
    # Fill screen with black
    screen.fill("black")
    
    # Update display
    pygame.display.flip()

    
if __name__ == "__main__":
    main()
