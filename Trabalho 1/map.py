import pygame, random
import time

from complexrobot import ComplexRobot
from simplerobot import SimpleRobot

class Map(object):

    def __init__(self, height, width, matrix, garbage_quantity):

        self.height = height
        self.width = width

        pygame.init()

        self.screen = pygame.display.set_mode([self.width, self.height])

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

        window = pygame.image.load('assets/wall_window.png')
        window = pygame.transform.scale(window, (self.block_size, self.block_size))

        wall = pygame.image.load('assets/wall.png')
        wall = pygame.transform.scale(wall, (self.block_size, self.block_size))

        wall_corner = pygame.image.load('assets/wall_corner.png')
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

        garbage = pygame.image.load('assets/trash.png')

        garbage_list = [garbage]

        for i in range(self.garbage_quantity):

            empty_space = 0

            while not empty_space:

                x = random.randint(1, len(self.map[0]) - 2)
                y = random.randint(1, len(self.map[0]) - 2)

                if self.map[x][y] == 0:

                    empty_space = 1
                    self.map[x][y] = 3

    def redraw_screen(self):

        self.screen.fill((255, 255, 255))

        self.create_map()
        self.create_walls()

        garbage = pygame.image.load('assets/trash.png')

        for x in range(1, len(self.map) - 1):

            for y in range(1, len(self.map[0]) - 1):

                # Garbage
                if self.map[x][y] == 3:

                    garbage_x = int(x * self.block_size + (self.block_size / 2) - (garbage.get_rect().width  / 2))
                    garbage_y = int(y * self.block_size + (self.block_size / 2) - (garbage.get_rect().height / 2))

                    self.screen.blit(garbage, (garbage_x , garbage_y))

                # Robot
                elif self.map[x][y] == 2:

                    rect = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)
                    pygame.draw.rect(self.screen, self.RED, rect, 1)


    def create_path(self):

        path = []

        # Draw snake path
        for x in range(1, len(self.map) - 1):

            if (x % 2 == 1):

                for y in range(1, len(self.map[0]) - 1):
                    path.append((x, y))

            else:

                for y in range(len(self.map[0]) - 2, 0, -1):
                    path.append((x, y))

        last = path[-1]

        # Go up
        while last[1] != 1:

            last = (last[0], last[1] - 1)
            path.append(last)

        # Go left
        while last[0] != 2:

            last = (last[0] - 1, last[1])
            path.append(last)

        return path

    def setup(self):

        self.screen.fill((255, 255, 255))

        self.create_map()
        self.create_walls()
        self.create_garbages()

        pygame.display.flip()

    def main(self):

        running = True
        finished = False

        self.redraw_screen()
        pygame.display.flip()

        while running:

            self.redraw_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            if not robot.finished:
                robot.move()

            elif not finished:

                print(f'Ponto: -> {robot.steps}')
                finished = True

            else:

                continue

            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    
    # matrix = [[1, 1, 11, 11, 1, 1],
    #           [1, 0,  0,  0, 0, 1],
    #           [1, 0,  0,  0, 0, 1],
    #           [1, 0,  0,  0, 0, 1],
    #           [1, 0,  0,  0, 0, 1],
    #           [1, 1,  1,  1, 1, 1]]

    matrix = [[1, 11, 1, 11, 11, 1, 11, 1],
              [1,  0, 0,  0,  0, 0,  0, 1],
              [1,  0, 0,  0,  0, 0,  0, 1],
              [1,  0, 0,  0,  0, 0,  0, 1],
              [1,  0, 0,  0,  0, 0,  0, 1],
              [1,  0, 0,  0,  0, 0,  0, 1],
              [1,  0, 0,  0,  0, 0,  0, 1],
              [1,  1, 1,  1,  1, 1,  1, 1]]

    # matrix = [[1, 1, 11, 1, 1],
    #           [1, 0,  0, 0, 1],
    #           [1, 0,  0, 0, 1],
    #           [1, 0,  0, 0, 1],
    #           [1, 1,  1, 1, 1]]

    robot = ComplexRobot(1, 1)
    game = Map(600, 600, matrix, 6)

    robot.set_map(game.map)
    robot.spawn()

    game.setup()
    game.main()

    # randomX = random.randint(1, len(matrix[0]) - 2)
    # randomY = random.randint(1, len(matrix[0]) - 2)

    # robot = SimpleRobot(randomX, randomY)
    # game = Map(600, 600, matrix, 6)

    # robot.set_path(game.create_path())
    # robot.set_map(game.map)
    # robot.spawn()

    # game.setup()
    # game.main()
    