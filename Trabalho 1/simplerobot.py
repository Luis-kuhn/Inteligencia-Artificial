import pygame

class SimpleRobot(object):

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.path = [] 
        self.map = []
        
        self.spriteState = ''
        self.dirty = False
        self.target = None
        self.finished = False

    def set_map(self, map):

        self.map = map

    def set_path(self, path):

        position = path[0]

        while position != (self.x, self.y):

            path.pop(0)
            path.append(position)

            position = path[0]

        print(path)

        self.path = path

    def spawn(self):

        self.map[self.x][self.y] = 2

    def move(self):

        pygame.time.wait(300)

        # Clean
        if self.dirty:

            print('Estado da percepcao: 1 Acao escolhida: Aspirar') 
            self.spriteState = 'clean'
            self.map[self.x][self.y] = 2
            self.dirty = False

            return

        self.target = self.path.pop(0)
        self.map[self.x][self.y] = 0

        if self.target[0] > self.x:

            print('Estado da percepcao: 0 Acao escolhida: Direita')
            self.spriteState = 'right'
            self.x += 1

        elif self.target[0] < self.x:

            print('Estado da percepcao: 0 Acao escolhida: Esquerda')
            self.spriteState = 'left'
            self.x -= 1

        elif self.target[1] > self.y:

            print('Estado da percepcao: 0 Acao escolhida: Abaixo')
            self.spriteState = 'down'
            self.y += 1

        elif self.target[1] < self.y:

            print('Estado da percepcao: 0 Acao escolhida: Acima')
            self.spriteState = 'up'
            self.y -= 1

        self.dirty = True if self.map[self.x][self.y] == 3 else False

        self.map[self.x][self.y] = 2
        self.path.append(self.target)

