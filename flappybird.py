### Packages ###
import pygame
from pygame.locals import *
import random

### Global Variables ###
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
SPEED_BACKGROUND = 2
SPEED_BIRD = 10
SPEED_GROUND = 10
GRAVITY = 1
FPS = 30
GROUND_WIDTH = SCREEN_WIDTH * 2
GROUND_HEIGHT = 100
PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 150

### Background ###
BACKGROUND = pygame.image.load('assets/sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND,(SCREEN_WIDTH,SCREEN_HEIGHT))

### Bird Constructor ###
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

### Ground Constructor ###
class Ground(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/sprites/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(GROUND_WIDTH, GROUND_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = pos_x
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT
    
    ### Update Ground ###
    def update(self):
        self.rect[0] -= SPEED_GROUND

### Background Constructor ###
class Background(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/sprites/background-day.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = pos_x
    
    ### Update Background ###
    def update(self):
        self.rect[0] -= SPEED_BACKGROUND

### Is Off Screen ###
def ground_is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])


### Start Game ###
pygame.init()
pygame.display.set_caption('Flappy Bird')
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # Make Windown

### Build Bird ###
bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

### Build Ground ###
ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground(GROUND_WIDTH * i)
    ground_group.add(ground)

### Build Ground ###
background_group = pygame.sprite.Group()
for i in range(2):
    background = Background(GROUND_WIDTH * i)
    background_group.add(background)

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
    
    #if ground_is_off_screen(background_group.sprites()[0]):
    #    background_group.remove(background_group.sprites()[0])
    #    new_background = Ground(SCREEN_WIDTH)
    #    background_group.add(new_background)

    if ground_is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])
        new_ground = Ground(GROUND_WIDTH - 20)
        ground_group.add(new_ground)

    #background_group.update()
    #background_group.draw(screen)
    bird_group.update()
    bird_group.draw(screen)
    ground_group.update()
    ground_group.draw(screen)

    pygame.display.update() # Update