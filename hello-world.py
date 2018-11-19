# pygame template skeleton for a brand new project

import pygame
import random


WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialializing the game
pygame.init()

# initialializing the sound
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# every moving game element is called a sprite
all_sprites = pygame.sprite.Group()

# game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # process input (events)

    for event in pygame.event.get():
        # check for termination of the game
        if event.type == pygame.QUIT:
            running = False

    # update
    all_sprites.update()

    # draw / render
    

    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything flip the display
    pygame.display.flip()


pygame.quit()
