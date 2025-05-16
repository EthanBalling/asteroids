import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize pygame, clock, and create a screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create and assign sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    # Create Object instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # Game loop
    while True:
        # Check for QUIT event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        '''
        # Update player position
        player.update(dt)
        '''
        # Update all sprites in the updatable group
        updatable.update(dt)
        
        # Check for collisions
        for asteroid in asteroids:
            # Check for player and asteroid collisions
            if asteroid.check_collision(player):
                print("Game Over!")
                sys.exit()
            # Check for shot and asteroid collisions
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.kill()
                    shot.kill()
        
        # Screen clearing
        screen.fill("black")
        
        '''
        # Draw the player
        player.draw(screen)
        '''
        # Draw all sprites in the drawable group
        for object in drawable:
            object.draw(screen)
        
        # Refresh and limit the framerate to 60 FPS
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

    '''
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    '''

if __name__ == "__main__":
    main()