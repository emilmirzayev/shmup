# pygame template skeleton for a brand new project
# opengameart.com useful website


import pygame
import random
import os


WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# setting up assets (game dev term for sounds and images)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # always convert image after creating it
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        # ignore the black rectange around the image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5
    
    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# initialializing the game
pygame.init()

# initialializing the sound
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# every moving game element is called a sprite
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
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
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # after drawing everything flip the display
    pygame.display.flip()


pygame.quit()
