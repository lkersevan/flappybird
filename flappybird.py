### Packages ###
import pygame
from pygame.locals import *
import random

### Global Variables ###
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
SPEED_BACKGROUND = 10
SPEED_BIRD = 10
GRAVITY = 1
FPS = 30
GROUND_WIDTH = 2 * SCREEN_HEIGHT
GROUND_HEIGHT = 100
PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 150

### Background ###
BACKGROUND = pygame.image.load('assets/sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND,(SCREEN_WIDTH,SCREEN_HEIGHT))

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                       pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha(),
                       pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
                       pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha()]
        self.speed = SPEED_BIRD
        self.current_image = 0
        self.image = pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = (SCREEN_WIDTH / 2) - (self.rect[2] / 2) 
        self.rect[1] = SCREEN_HEIGHT / 2 - (self.rect[3] / 2)
    
    ### Update Bird Move ###
    def update(self):
        self.current_image = (self.current_image + 1) % 4
        self.image = self.images[self.current_image]
        self.speed += GRAVITY
        self.rect[1] += self.speed
    
    ### Bump ###
    def bump(self):
        self.speed = -SPEED_BIRD

### Start Game ###
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # Make Windown

### Bird Constructor ###
bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

clock = pygame.time.Clock()

### Update Screen ###
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()
    
    screen.blit(BACKGROUND,(0,0)) # Make Background
    
    bird_group.update()
    bird_group.draw(screen)

    pygame.display.update() # Update