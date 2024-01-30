import pygame

class ComplexRobot(object):

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.path = []
        self.map = []
        self.garbages_positions = []
        self.garbages_distances = []

        self.sprite = ''

        self.steps = 0
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

    def spawn(self):
        '''
        Coloca o robô no mapa.
        '''

        self.map[self.y][self.x] = 2

    def find_garbages(self):
        '''
        Procura os lixos no mapa e salva suas posições.
        '''

        positions_list = []

        for x in range(len(self.map)):

            for y in range(len(self.map[0])):

                if self.map[y][x] == 3:

                    positions_list.append((x, y))

        if not positions_list:

            self.finished = True
            self.state = 'finished'

            return

        self.garbages_positions = positions_list

    def calculate_distances(self):
        '''
        Calcula as distâncias entre o robô e todos os lixos encontrados.
        '''

        distances_list = []

        for x, y in self.garbages_positions:

            distances_list.append(abs(self.x - x) + abs(self.y - y))

        self.garbages_distances = distances_list

    def find_closest(self):
        '''
        Procura o lixo mais próximo.
        '''

        self.find_garbages()
        self.calculate_distances()

        closest = min(self.garbages_distances)

        index = self.garbages_distances.index(closest)
        closest_position = self.garbages_positions[index]

        self.target = closest_position

    def move(self):
        '''
        Move o robô pelo mapa.
        '''

        if not self.finished:

            # Se há um lixo alvo...
            if self.target is not None:

                pygame.time.wait(300)

                self.map[self.y][self.x] = 0
                self.steps += 1

                # Retira o lixo
                if self.dirty:

                    print('Estado da percepcao: 1 Acao escolhida: Aspirar') 
                    self.map[self.y][self.x] = 2
                    self.state = 'clean'

                    self.dirty = False
                    self.target = None

                    return

                # Direita
                if self.target[0] > self.x:

                    print('Estado da percepcao: 0 Acao escolhida: Direita')
                    self.state = 'right'
                    self.x += 1

                # Esquerda
                elif self.target[0] < self.x:

                    print('Estado da percepcao: 0 Acao escolhida: Esquerda')
                    self.state = 'left'
                    self.x -= 1

                # Abaixo
                elif self.target[1] > self.y:

                    print('Estado da percepcao: 0 Acao escolhida: Abaixo')
                    self.state = 'down'
                    self.y += 1

                # Acima
                elif self.target[1] < self.y:

                    print('Estado da percepcao: 0 Acao escolhida: Acima')
                    self.state = 'up'
                    self.y -= 1
                    
                self.dirty = True if self.map[self.y][self.x] == 3 else False

                self.map[self.y][self.x] = 2
                
            # Se não há...
            else:

                # Procura o menor lixo e anda
                self.find_closest()
                self.move()
