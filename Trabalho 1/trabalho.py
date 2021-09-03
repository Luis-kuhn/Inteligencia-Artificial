import pygame, random
from pygame.locals import *
import numpy as np

# matriz_inicio=np.array([[1, 11, 1, 11, 11, 1, 11, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  1, 1,  1,  1, 1,  1, 1]])

matriz_inicio=np.array([[1, 1, 11, 11, 1, 1],
                        [1, 0,  0,  0, 0, 1],
                        [1, 0,  0,  0, 0, 1],
                        [1, 0,  0,  0, 0, 1],
                        [1, 0,  0,  0, 0, 1],
                        [1, 1,  1,  1, 1, 1]])

# matriz_inicio=np.array([[1, 1, 11, 1, 1],
#                         [1, 0,  0, 0, 1],
#                         [1, 0,  0, 0, 1],
#                         [1, 0,  0, 0, 1],
#                         [1, 1,  1, 1, 1]])

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
blockSize = WINDOW_WIDTH // len(matriz_inicio[0])
QTD_LIXO = 6
GRID = False

pygame.init()
screen = pygame.display.set_mode([WINDOW_HEIGHT, WINDOW_WIDTH])

running = True
screen.fill((255, 255, 255))

def colocaLixo():
    lixo = pygame.image.load('assets/lixo.png')
    papel = pygame.image.load('assets/papel.png')
    for i in range(QTD_LIXO):
        x = random.randint(1, len(matriz_inicio[0])-2)
        y = random.randint(1, len(matriz_inicio[0])-2)
        tipoLixo = random.randint(0, 1)
        if tipoLixo == 1:
            screen.blit(papel,(x*blockSize, y*blockSize))
        else:
            screen.blit(lixo,(x*blockSize, y*blockSize))

def paredes(x, y):
    janela = pygame.image.load('assets/ParedeJanela.png')
    janela = pygame.transform.scale(janela, (blockSize, blockSize))

    parede = pygame.image.load('assets/parede2.png')
    parede = pygame.transform.scale(parede, (blockSize, blockSize))

    cantoParede = pygame.image.load('assets/cantoParede.png')
    cantoParede = pygame.transform.scale(cantoParede, (blockSize, blockSize))
    
    if matriz_inicio[y][x] == 11:
        screen.blit(janela,(x*blockSize, y*blockSize,blockSize,blockSize))
        
    if matriz_inicio[y][x] == 1:
        if (x==0 or x == len(matriz_inicio[0])-1):
            parede2 = pygame.transform.rotate(parede, 90)
            screen.blit(parede2,(x*blockSize, y*blockSize,blockSize,blockSize))
        else:
            screen.blit(parede,(x*blockSize, y*blockSize,blockSize,blockSize))
        
        if (x==0 and y==0):
            screen.blit(cantoParede,(x*blockSize, y*blockSize,blockSize,blockSize))
            
        if(y==0  and x == len(matriz_inicio[0])-1):
            cantoParede2 = pygame.transform.rotate(cantoParede, -90)
            screen.blit(cantoParede2,(x*blockSize, y*blockSize,blockSize,blockSize))
        
        if(x==0  and y == len(matriz_inicio)-1):
            cantoParede2 = pygame.transform.rotate(cantoParede, 90)
            screen.blit(cantoParede2,(x*blockSize, y*blockSize,blockSize,blockSize))
            
        if(y == len(matriz_inicio)-1 and x == len(matriz_inicio)-1):
            cantoParede2 = pygame.transform.rotate(cantoParede, 180)
            screen.blit(cantoParede2,(x*blockSize, y*blockSize,blockSize,blockSize))
            
def drawGrid():
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

if (GRID):
    drawGrid()

for x in range(len(matriz_inicio)):
    for y in range(len(matriz_inicio[0])):
        paredes(x, y)
            
colocaLixo()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
