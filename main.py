import pygame
from constants import *
from player import Player

def main():
    # Initialize pygame, clock, and create a screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create and set the initial position of the player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    # Game loop
    while True:
        # Check for QUIT event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Screen
        screen.fill("black")
        
        # Draw the player
        player.draw(screen)
        
        # Refresh and limit the framerate to 60 FPS
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        
        
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()