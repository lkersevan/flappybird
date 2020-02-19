### Pacotes ###
import pygame
from pygame.locals import *

### Variáveis Globais ###
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800

### Inicializa Jogo ###
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # Criando a janela
### Parâmetros do Fundo do Jogo ###
BACKGROUND = pygame.image.load('assets/sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND,(SCREEN_WIDTH,SCREEN_HEIGHT))

### Laço Para Atualizar a Tela ###
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    screen.blit(BACKGROUND,(0,0)) # Cria o fundo de tela
    pygame.display.update()