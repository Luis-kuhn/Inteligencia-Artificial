import pygame

class ComplexRobot(object):

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.path = []
        self.map = []
        self.garbages_positions = []
        self.garbages_distances = []

        self.steps = 0
        self.spriteState = ''

        self.dirty = False
        self.target = None
        self.finished = False

    def set_map(self, map):

        self.map = map

    def spawn(self):

        self.map[self.x][self.y] = 2

    def find_garbages(self):

        positions_list = []

        for x in range(len(self.map)):

            for y in range(len(self.map[0])):

                if self.map[x][y] == 3:

                    positions_list.append((x, y))

        if not positions_list:

            print('finished')
            self.finished = True
            self.spriteState = 'finished'

            return

        self.garbages_positions = positions_list

    def calculate_distances(self):

        distances_list = []

        for x, y in self.garbages_positions:

            distances_list.append(abs(self.x - x) + abs(self.y - y))

        self.garbages_distances = distances_list

    def find_closest(self):

        self.find_garbages()
        self.calculate_distances()

        closest = min(self.garbages_distances)

        index = self.garbages_distances.index(closest)
        closest_position = self.garbages_positions[index]

        self.target = closest_position

    def move(self):

        if not self.finished:

            if self.target is not None:

                pygame.time.wait(300)

                self.map[self.x][self.y] = 0
                self.steps += 1

                if self.dirty:

                    print('Estado da percepcao: 1 Acao escolhida: Aspirar', self.steps) 
                    self.map[self.x][self.y] = 2
                    self.spriteState = 'clean'

                    self.dirty = False
                    self.target = None

                    return

                if self.target[0] > self.x:

                    print('Estado da percepcao: 0 Acao escolhida: Direita', self.steps)
                    self.spriteState = 'right'
                    self.x += 1

                elif self.target[0] < self.x:

                    print('Estado da percepcao: 0 Acao escolhida: Esquerda', self.steps)
                    self.spriteState = 'left'
                    self.x -= 1

                elif self.target[1] > self.y:

                    print('Estado da percepcao: 0 Acao escolhida: Abaixo', self.steps)
                    self.spriteState = 'down'
                    self.y += 1

                elif self.target[1] < self.y:

                    print('Estado da percepcao: 0 Acao escolhida: Acima', self.steps)
                    self.spriteState = 'up'
                    self.y -= 1
                    
                self.dirty = True if self.map[self.x][self.y] == 3 else False

                self.map[self.x][self.y] = 2
                

            else:

                self.find_closest()
                self.move()
