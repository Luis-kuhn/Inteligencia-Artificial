import pygame, random
from pygame.locals import *
import numpy as np
import time

class Robot(object):

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.map = []
        self.garbages_positions = []
        self.garbages_distances = []

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

                pygame.time.wait(1500)
                print(self.target)

                self.map[self.x][self.y] = 0

                if self.target[0] > self.x:

                    print('Direita')
                    self.x += 1

                elif self.target[0] < self.x:

                    print('Esquerda')
                    self.x -= 1

                elif self.target[1] > self.y:

                    print('Baixo')
                    self.y += 1

                elif self.target[1] < self.y:

                    print('Cima')
                    self.y -= 1

                else:

                    print('Limpar') 
                    self.map[self.target[0]][self.target[1]] = 0
                    self.target = None
                    
                self.map[self.x][self.y] = 2

                pygame.time.wait(1500)

            else:

                self.find_closest()
                self.move()

class Map(object):

    def __init__(self, height, width, matrix, garbage_quantity):

        self.height = height
        self.width = width

        pygame.init()

        self.screen = pygame.display.set_mode([self.width + 300, self.height])

        self.map = matrix
        self.garbage_quantity = garbage_quantity
        self.block_size = self.width // len(self.map[0])

        self.BLACK = (  0,   0,   0)
        self.RED   = (255,   0,   0)
        self.WHITE = (200, 200, 200)

    def create_map(self):

        for x in range(0, self.width, self.block_size):

            for y in range(0, self.height, self.block_size):

                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, self.WHITE, rect, 1)

    def create_walls(self):

        window = pygame.image.load('assets/ParedeJanela.png')
        window = pygame.transform.scale(window, (self.block_size, self.block_size))

        wall = pygame.image.load('assets/parede2.png')
        wall = pygame.transform.scale(wall, (self.block_size, self.block_size))

        wall_corner = pygame.image.load('assets/cantoParede.png')
        wall_corner = pygame.transform.scale(wall_corner, (self.block_size, self.block_size))
        
        for x in range(len(self.map)):

            for y in range(len(self.map[0])):

                # Window
                if self.map[y][x] == 11:
                    self.screen.blit(window, (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
                    
                # Wall
                if self.map[y][x] == 1:

                    if x == 0 or x == len(self.map[0]) - 1:
                        rotated_wall = pygame.transform.rotate(wall, 90)
                        self.screen.blit(rotated_wall, (x * self.block_size, y * self.block_size, self.block_size, self.block_size))

                    else:
                        self.screen.blit(wall, (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
                    
                    if x == 0 and y == 0:
                        self.screen.blit(wall_corner, (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
                        
                    if y == 0  and x == len(self.map[0]) - 1:
                        rotated_wall_corner = pygame.transform.rotate(wall_corner, -90)
                        self.screen.blit(rotated_wall_corner, (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
                    
                    if x==0  and y == len(self.map) - 1:
                        rotated_wall_corner = pygame.transform.rotate(wall_corner, 90)
                        self.screen.blit(rotated_wall_corner, (x * self.block_size, y * self.block_size, self.block_size, self.block_size))
                        
                    if y == len(self.map) - 1 and x == len(self.map) - 1:
                        rotated_wall_corner = pygame.transform.rotate(wall_corner, 180)
                        self.screen.blit(rotated_wall_corner, (x * self.block_size, y * self.block_size, self.block_size, self.block_size))

    def create_garbages(self):

        garbage = pygame.image.load('assets/lixo.png')
        #paper = pygame.image.load('assets/papel.png')

        garbage_list = [garbage]

        for i in range(self.garbage_quantity):

            empty_space = 0

            while not empty_space:

                x = random.randint(1, len(self.map[0]) - 2)
                y = random.randint(1, len(self.map[0]) - 2)

                if self.map[x][y] == 0:

                    empty_space = 1
                    self.map[x][y] = 3

                    # garbage_type = 0

                    # x = int(x * self.block_size + (self.block_size / 2) - (garbage_list[garbage_type].get_rect().width  / 2))
                    # y = int(y * self.block_size + (self.block_size / 2) - (garbage_list[garbage_type].get_rect().height / 2))

                    # self.screen.blit(garbage_list[garbage_type], (x , y))

    def redraw_screen(self):

        self.screen.fill((255, 255, 255))

        self.create_map()
        self.create_walls()

        garbage = pygame.image.load('assets/lixo.png')

        for x in range(1, len(self.map) - 1):

            for y in range(1, len(self.map[0]) - 1):

                if self.map[x][y] == 3:

                    garbage_x = int(x * self.block_size + (self.block_size / 2) - (garbage.get_rect().width  / 2))
                    garbage_y = int(y * self.block_size + (self.block_size / 2) - (garbage.get_rect().height / 2))

                    self.screen.blit(garbage, (garbage_x , garbage_y))

                elif self.map[x][y] == 2:

                    rect = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)
                    pygame.draw.rect(self.screen, self.RED, rect, 1)

                else:

                    rect = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)
                    pygame.draw.rect(self.screen, self.WHITE, rect, 1)

    def setup(self):

        self.screen.fill((255, 255, 255))

        self.create_map()
        self.create_walls()
        self.create_garbages()

        pygame.display.flip()

    def main(self):

        running = True
        #self.setup()

        while running:

            if not robot.finished:
                robot.move()

            self.redraw_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    
    matrix = [[1, 1, 11, 11, 1, 1],
              [1, 0,  0,  0, 0, 1],
              [1, 0,  0,  0, 0, 1],
              [1, 0,  0,  0, 0, 1],
              [1, 0,  0,  0, 0, 1],
              [1, 1,  1,  1, 1, 1]]

# matrix=np.array([[1, 11, 1, 11, 11, 1, 11, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  0, 0,  0,  0, 0,  0, 1],
#                         [1,  1, 1,  1,  1, 1,  1, 1]])



# matrix=np.array([[1, 1, 11, 1, 1],
#                         [1, 0,  0, 0, 1],
#                         [1, 0,  0, 0, 1],
#                         [1, 0,  0, 0, 1],
#                         [1, 1,  1, 1, 1]])

    robot = Robot(1, 1)
    game = Map(600, 600, matrix, 6)
    robot.set_map(game.map)
    robot.spawn()

    game.setup()

    time.sleep(2)
    game.main()
    
