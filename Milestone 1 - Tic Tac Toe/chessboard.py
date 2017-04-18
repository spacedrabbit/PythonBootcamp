from IPython.display import clear_output
from player import *

class Board:
    board = []

    def __init__(self):
        self.__build_board()

    def __build_board(self):
        self.board = [[BoardSquare(i) for i in range(1, 4)],
                      [BoardSquare(i) for i in range(4, 7)],
                      [BoardSquare(i) for i in range(7, 10)] ]

    def display_board(self):
        for row in self.board:
            s = row[0].update_square() + row[1].update_square() + row[2].update_square()
            print('%s' % s)

    def update_square(self, position, player):
        position_tuple = self.position_to_tuple(position)
        row = position_tuple[0]
        col = position_tuple[1]

        if self.space_check(row, col):
            square = self.board[row][col]
            square.change_owner(player)
            return True
        else:
            print("Square already played, try again")
            return False

    def space_check(self, row, col):
        square = self.board[row][col]
        return True if square.ownedby == None else False

    def space_owner(self, position):
        position_tuple = self.position_to_tuple(position)
        row = position_tuple[0]
        col = position_tuple[1]

        square = self.board[row][col]
        return square.ownedby

    def position_to_tuple(self, position):
        row = (position / 3)
        col = position % 3
        return (row, col)

    def return_rows(self):
        return [[self.board[0][0], self.board[0][1], self.board[0][2]],
                [self.board[1][0], self.board[1][1], self.board[1][2]],
                [self.board[2][0], self.board[2][1], self.board[2][2]]
                ]

    def return_cols(self):
        return [[self.board[0][0], self.board[1][0], self.board[2][0]],
                [self.board[0][1], self.board[1][1], self.board[2][1]],
                [self.board[0][2], self.board[1][2], self.board[2][2]] ]

    def return_diag(self):
        return [[self.board[0][0], self.board[1][1], self.board[2][2]],
                [self.board[2][0], self.board[1][1], self.board[0][2]] ]

class BoardSquare:
    ownedby = Player
    position = -1

    def __init__(self, position):
        self.ownedby = None
        self.position = position

    def change_owner(self, player):
        self.ownedby = player

    def update_square(self):
        if self.ownedby != None:
            return "[{m}]".format(m=self.ownedby.marker)
        return "[{p}]".format(p=self.position)