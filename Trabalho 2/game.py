import pygame
import time
from computer import Computer

class Screen(object):

    def __init__(self, height, width):

        self.height = height
        self.width = width
        
        pygame.init()

        self.screen = pygame.display.set_mode([self.width, self.height])

        self.BLACK     = (  0,   0,   0)
        self.RED       = (255,   0,   0)
        self.GRAY      = (200, 200, 200)
        self.LIGHTGRAY = (230, 230, 230)
        self.WHITE     = (255, 255, 255)
        self.BLUE      = ( 52, 122, 235)
        self.DARKBLUE  = ( 33,  78, 150)

        self.game_running = False
        self.block_size = 115
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.turn = 'X'
        self.game_mode = 1

        self.ties = 0
        self.wins_x = 0
        self.wins_o = 0

        self.computerO = Computer('O')
        self.computerX = Computer('X')

    def draw_button(self, message, x, y, w, h, inactive, active, font_color, border, action = None, parameters = None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:

            if border: pygame.draw.rect(self.screen, self.BLACK, (x - 2, y - 2, w + 4, h + 4))
            pygame.draw.rect(self.screen, active, (x, y, w, h))

            if click[0] == 1 and action is not None:
                if parameters is not None: action(parameters)
                else: action()

            else:
                pygame.draw.rect(self.screen, active, (x, y, w, h))

        else:

            if border: pygame.draw.rect(self.screen, self.BLACK, (x - 2, y - 2, w + 4, h + 4))
            pygame.draw.rect(self.screen, inactive, (x, y, w, h))

        font = pygame.font.Font("freesansbold.ttf", 20)
        textBlock = font.render(message, 1, font_color)

        text_height = float(textBlock.get_height())
        text_width = float(textBlock.get_width())

        self.screen.blit(textBlock, ((x + (w / 2)) - text_width / 2, (y + (h / 2) - text_height / 2)))

    def start_game(self, mode):

        self.game_running = True
        self.game_mode = mode
        time.sleep(1)

    def run(self):

        # player x player
        if (self.game_mode == 1):
            self.screen.fill(self.WHITE)
            self.draw_game()

        # player x ai
        if self.game_mode == 2:

            if self.turn == 'O':

                time.sleep(0.5)
                print(self.board.copy())
                move = self.computerO.move(self.board.copy())
                self.add_mark(move[0], move[1])

            self.screen.fill(self.WHITE)
            self.draw_game()

        # ai x ai
        if self.game_mode == 3:
            
            if self.turn == 'O':

                time.sleep(0.5)
                print(self.board.copy())
                move = self.computerO.move(self.board.copy())
                self.add_mark(move[0], move[1])

            elif self.turn == 'X':

                time.sleep(0.5)
                print(self.board.copy())
                move = self.computerX.move(self.board.copy())
                self.add_mark(move[0], move[1])

            self.screen.fill(self.WHITE)
            self.draw_game()

    def check_win(self):

        # columns
        for row in range(3):
            if len(set([self.board[i][row] for i in range(3)])) == 1:
                if self.board[0][row] != '': return True

        # row
        for row in self.board:
            if len(set(row)) == 1:
                if row[0] != '': return True

        # diagonal \
        if len(set([self.board[i][i] for i in range(len(self.board))])) == 1:
            if self.board[0][0] != '': return True

        # diagonal /
        if len(set([self.board[i][len(self.board)-i-1] for i in range(len(self.board))])) == 1:
            if self.board[0][len(self.board)-1] != '': return True

        remaining = 9
        for row in self.board:
            for space in row:
                if space != '':
                    remaining -= 1

        if remaining == 0:
            return None

        return False


    def restart(self):

        self.draw_game()
        pygame.display.flip()
        time.sleep(1)

        self.board = [['', '', ''], ['', '', ''], ['', '', '']]

    def add_mark(self, x, y):

        self.board[y][x] = self.turn
        result = self.check_win()

        # Empate
        if result is None:
            self.ties += 1
            self.restart()

        # Vitória
        elif result:
            if self.turn == 'X':
                self.wins_x += 1
            else:
                self.wins_o += 1

            self.restart()

        self.turn = 'X' if self.turn == 'O' else 'O'

    def draw_mark(self, x, y, block):

        if self.board[y][x]:

            sprite = pygame.image.load('assets/x.png') if self.board[y][x] == 'X' else pygame.image.load('assets/o.png')
            sprite = pygame.transform.scale(sprite, (50, 50))

            sprite_x = int(block.x + (self.block_size / 2) - (sprite.get_rect().width  / 2))
            sprite_y = int(block.y + (self.block_size / 2) - (sprite.get_rect().height / 2))

            self.screen.blit(sprite, (sprite_x, sprite_y))

    def draw_board(self):

        board = pygame.draw.rect(self.screen, self.GRAY, (20, 150, 360, 360))

        for y in range(3):

            padding_y = 0
            if y: padding_y = 7.5

            for x in range(3):

                padding_x = 0
                if x: padding_x = 7.5

                block_x = board.x + (self.block_size * x) + (padding_x * x)
                block_y = board.y + (self.block_size * y) + (padding_y * y)

                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                block = pygame.draw.rect(self.screen, self.WHITE, (block_x, block_y, self.block_size, self.block_size))

                if block_x + self.block_size > mouse[0] > block_x and block_y + self.block_size > mouse[1] > block_y:

                    if not self.board[y][x]:

                        block = pygame.draw.rect(self.screen, self.LIGHTGRAY, (block_x, block_y, self.block_size, self.block_size))

                        if click[0] == 1:
                            self.add_mark(x, y)
                            time.sleep(0.1)

                        else:
                            block = pygame.draw.rect(self.screen, self.LIGHTGRAY, (block_x, block_y, self.block_size, self.block_size))

                self.draw_mark(x, y, block)

    def draw_scores(self):

        font = pygame.font.Font("freesansbold.ttf", 20)

        # X score
        block = pygame.draw.rect(self.screen, self.WHITE, (20, 20, 100, 100))
        sprite_x = pygame.image.load('assets/x.png')
        sprite_x = pygame.transform.scale(sprite_x, (50, 50))

        textBlock = font.render(str(self.wins_x), 1, self.BLACK)
        text_height = float(textBlock.get_height())
        text_width = float(textBlock.get_width())

        self.screen.blit(sprite_x, (block.x + 25, 20))
        self.screen.blit(textBlock, (block.x + 50 - text_width / 2, 100 - text_height / 2))

        # O score
        block = pygame.draw.rect(self.screen, self.WHITE, (150, 20, 100, 100))
        sprite_o = pygame.image.load('assets/o.png')
        sprite_o = pygame.transform.scale(sprite_o, (50, 50))

        textBlock = font.render(str(self.wins_o), 1, self.BLACK)
        text_height = float(textBlock.get_height())
        text_width = float(textBlock.get_width())

        self.screen.blit(sprite_o, (block.x + 25, 20))
        self.screen.blit(textBlock, (block.x + 50 - text_width / 2, 100 - text_height / 2))

        # draw score
        block = pygame.draw.rect(self.screen, self.WHITE, (280, 20, 100, 100))
        sprite_scale = pygame.image.load('assets/scale.png')
        sprite_scale = pygame.transform.scale(sprite_scale, (50, 50))

        textBlock = font.render(str(self.ties), 1, self.BLACK)
        text_height = float(textBlock.get_height())
        text_width = float(textBlock.get_width())

        self.screen.blit(sprite_scale, (block.x + 25, 20))
        self.screen.blit(textBlock, (block.x + 50 - text_width / 2, 100 - text_height / 2))


    def draw_game(self):

        self.draw_scores()
        self.draw_board()

    def main_menu(self):

        # background
        background_rectangle = pygame.Surface((2, 2))
        pygame.draw.line(background_rectangle, (237, 144, 78), (0, 0), (1, 0))
        pygame.draw.line(background_rectangle, (237, 78, 102), (0, 1), (1, 1))
        background_rectangle = pygame.transform.smoothscale(background_rectangle, (self.screen.get_rect().width, self.screen.get_rect().height))
        self.screen.blit(background_rectangle, self.screen.get_rect())

        # logo
        logo = pygame.image.load('assets/logo.png').convert_alpha()
        logo = pygame.transform.scale(logo, (300, 300))
        self.screen.blit(logo, (50, 50)) 

        # buttons
        self.draw_button('2 Jogadores', 50, 440, 300, 50, self.WHITE, self.GRAY, self.BLACK, True, self.start_game, 1)
        self.draw_button('1 Jogador', 50, 510, 300, 50, self.WHITE, self.GRAY, self.BLACK, True, self.start_game, 2)
        self.draw_button('IA vs IA', 50, 580, 300, 50, self.WHITE, self.GRAY, self.BLACK, True, self.start_game, 3)

    def main(self):

        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.game_running:
                self.main_menu()

            else:
                self.run()

            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':

    mapa = Screen(700, 400)
    mapa.main()
