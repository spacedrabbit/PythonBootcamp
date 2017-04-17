from __future__ import print_function

class Board:
    board = []

    def __init__(self):
        self.__build_board()

    def __build_board(self):
        self.board = [['[1]', '[2]', '[3]'],
                      ['[4]', '[5]', '[6]'],
                      ['[7]', '[8]', '[9]']]

    def display_board(self):
        for row in self.board:
            print(row)


class Player:
    marker = str

    def __init__(self, marker):
        self.marker = marker


class TTTGame:
    board = None
    player1 = Player("X")
    player2 = Player("O")
    currentplayer = Player

    def __init__(self):
        self.board = Board()
        self.board.display_board()

        self.currentplayer = self.player1
        self.start()

    def start(self):
        choice = None

        while choice is None:
            player_input = raw_input("Enter a value (1-9): ")
            adjusted = int(player_input) - 1
            if 0 <= adjusted <= 8:
                self.place_marker(self.board, self.currentplayer.marker, adjusted)
            elif adjusted == int("q"):
                exit()
            else:
                print("Invalid Selection")
                self.start()

    def place_marker(self, board, marker, position):
        row = (position / 3)
        col = position % 3
        board.board[row][col] = "[{marker}]".format(marker=marker)
        board.display_board()


game = TTTGame()
