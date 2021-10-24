class Computer(object):

    def __init__(self, mark):

        self.mark = mark

    def is_end(self, board):
        # Vertical win
        for i in range(0, 3):
            if (board[0][i] != '' and
                board[0][i] == board[1][i] and
                board[1][i] == board[2][i]):
                return board[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (board[i] == ['X', 'X', 'X']):
                return 'X'
            elif (board[i] == ['O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (board[0][0] != '' and
            board[0][0] == board[1][1] and
            board[0][0] == board[2][2]):
            return board[0][0]

        # Second diagonal win
        if (board[0][2] != '' and
            board[0][2] == board[1][1] and
            board[0][2] == board[2][0]):
            return board[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (board[i][j] == ''):
                    return None

        # It's a tie!
        return ''

    def max(self, board):

        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None

        result = self.is_end(board)

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == 'X':
            return (-1, 0, 0) if self.mark == 'O' else (1, 0, 0)
        elif result == 'O':
            return (1, 0, 0) if self.mark == 'O' else (-1, 0, 0)
        elif result == '':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == '':

                    board[i][j] = 'O' if self.mark == 'O' else 'X'
                    (m, min_i, min_j) = self.min(board)

                    if m > maxv:
                        maxv = m
                        px = i
                        py = j

                    board[i][j] = ''

        return (maxv, px, py)

    def min(self, board):

        # Possible values for minv are:
        # -1 - win
        # 0  - a tie
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        qx = None
        qy = None

        result = self.is_end(board)

        if result == 'X':
            return (-1, 0, 0) if self.mark == 'O' else (1, 0, 0)
        elif result == 'O':
            return (1, 0, 0) if self.mark == 'O' else (-1, 0, 0)
        elif result == '':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == '':
                    board[i][j] = 'X' if self.mark == 'O' else 'O'
                    (m, max_i, max_j) = self.max(board)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    board[i][j] = ''

        return (minv, qx, qy)

    def move(self, board):

        (m, px, py) = self.max(board)

        print(self.mark)
        print(board)
        return (px, py)