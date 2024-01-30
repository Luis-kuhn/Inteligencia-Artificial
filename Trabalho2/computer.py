import random

# Authors: Christyelen Kramel, Luis Augusto Kühn, Thomas Ricardo Reinke e Yuri Matheus Hartmann

class Computer(object):

    def __init__(self, mark):

        self.mark = mark
        self.board = []

    def check_empty(self):
        '''
        Função responsável por verificar se o tabuleiro está vazio.
        '''

        remaining = 9
        for row in self.board:
            for space in row:
                if space != '':
                    remaining -= 1

        if remaining == 9:
            return True

        return False

    def check_win(self):
        '''
        Função responsável por verificar se há um vencedor e retorná-lo.
        '''
        
        # columns
        for row in range(3):
            if len(set([self.board[i][row] for i in range(3)])) == 1:
                if self.board[0][row] != '': return self.board[0][row]

        # row
        for row in self.board:
            if len(set(row)) == 1:
                if row[0] != '': return row[0]

        # diagonal \
        if len(set([self.board[i][i] for i in range(len(self.board))])) == 1:
            if self.board[0][0] != '': return self.board[0][0]

        # diagonal /
        if len(set([self.board[i][len(self.board) - i - 1] for i in range(len(self.board))])) == 1:
            if self.board[0][len(self.board) - 1] != '': return self.board[0][len(self.board) - 1]

        # check not full
        for row in self.board:
            for space in row:
                if space == '':
                    return None
            
        # tie
        return ''

    def max(self):
        '''
        Função responsável pelo MAX.
        '''

        max_value = -2
        coord_x = 0
        coord_y = 0

        result = self.check_win()

        if result == 'X':
            return (-1, 0, 0) if self.mark == 'O' else (1, 0, 0)

        elif result == 'O':
            return (1, 0, 0) if self.mark == 'O' else (-1, 0, 0)

        elif result == '':
            return (0, 0, 0)

        for x in range(3):
            for y in range(3):
                if self.board[y][x] == '':

                    self.board[y][x] = 'O' if self.mark == 'O' else 'X'
                    (min_value, _, _) = self.min()

                    if min_value > max_value:
                        max_value = min_value
                        coord_x = x
                        coord_y = y

                    self.board[y][x] = ''

        return (max_value, coord_x, coord_y)

    def min(self):
        '''
        Função responsável pelo MIN.
        '''

        min_value = 2
        coord_x = 0
        coord_y = 0

        result = self.check_win()

        if result == 'X':
            return (-1, 0, 0) if self.mark == 'O' else (1, 0, 0)

        elif result == 'O':
            return (1, 0, 0) if self.mark == 'O' else (-1, 0, 0)

        elif result == '':
            return (0, 0, 0)

        for x in range(3):
            for y in range(3):

                if self.board[y][x] == '':
                    self.board[y][x] = 'X' if self.mark == 'O' else 'O'
                    (max_value, _, _) = self.max()

                    if max_value < min_value:
                        min_value = max_value
                        coord_x = x
                        coord_y = y

                    self.board[y][x] = ''

        return (min_value, coord_x, coord_y)

    def move(self, board):
        '''
        Função responsável por retornar uma jogada.
        '''

        self.board = board

        if self.check_empty():
            return (random.randint(0, 2), random.randint(0, 2))

        else:
            (m, coord_x, coord_y) = self.max()
            return (coord_x, coord_y)