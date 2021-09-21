import pygame

class SimpleRobot(object):

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.path = [] 
        self.map = []

        self.sprite = ''
        
        self.state = 'down'

        self.dirty = False
        self.target = None
        self.finished = False

    def get_direction(self):
        '''
        Redefine a sprite baseado na direção.
        '''

        if(self.state == 'down'):
            self.sprite = pygame.image.load('assets/robot/down.png')

        elif(self.state == 'up'):
            self.sprite = pygame.image.load('assets/robot/up.png')

        elif(self.state == 'right'):
            self.sprite = pygame.image.load('assets/robot/right.png')

        elif(self.state == 'left'):
            self.sprite = pygame.image.load('assets/robot/left.png')

        elif(self.state == 'clean'):
            self.sprite = pygame.image.load('assets/robot/clean.png')

        elif(self.state == 'finished'):
            self.sprite = pygame.image.load('assets/robot/finished.png')

    def set_map(self, map):
        '''
        Seta o mapa.
        '''

        self.map = map

    def set_path(self, path):
        '''
        Seta o caminho fixo.
        '''

        position = path[0]

        while position != (self.x, self.y):

            path.pop(0)
            path.append(position)

            position = path[0]

        self.path = path

    def spawn(self):
        '''
        Coloca o robô no mapa.
        '''

        self.map[self.y][self.x] = 2

    def move(self):
        '''
        Move o robô pelo mapa.
        '''

        pygame.time.wait(300)

        # Retira o lixo
        if self.dirty:

            self.state = 'clean'
            self.map[self.y][self.x] = 2
            self.dirty = False

            return

        self.target = self.path.pop(0)
        self.map[self.y][self.x] = 0

        # Direita
        if self.target[0] > self.x:

            self.state = 'right'
            self.x += 1

        # Esquerda
        elif self.target[0] < self.x:

            self.state = 'left'
            self.x -= 1

        # Abaixo
        elif self.target[1] > self.y:

            self.state = 'down'
            self.y += 1

        # Acima
        elif self.target[1] < self.y:

            self.state = 'up'
            self.y -= 1

        self.dirty = True if self.map[self.y][self.x] == 3 else False

        self.map[self.y][self.x] = 2
        self.path.append(self.target)

