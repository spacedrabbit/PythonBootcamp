from __future__ import print_function
import random
from player import Player
from chessboard import *

class TTTGame:
    board = None
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")
    currentplayer = Player

    def __init__(self):
        self.board = Board()
        self.board.display_board()

        self.choose_random_player()
        self.start()

    def start(self):
        choice = None # todo: change this to win condition not true

        while choice is None:
            print("It is {pl}'s Turn".format(pl=self.currentplayer.playerName))
            player_input = raw_input("Enter a value (1-9): ") # problem suggests using 1-9, but
            adjusted = int(player_input) - 1 # working w/ zero index is easier, so adjustment is made
            if 0 <= adjusted <= 8: # checks between 0/8 but crashes on any other char
                self.place_marker(self.board, self.currentplayer.marker, adjusted)
            else:
                print("Invalid Selection")
                self.start()

    def place_marker(self, board, marker, position):
        row = (position / 3)
        col = position % 3

        board.update_square(position, self.currentplayer)
        board.display_board()
        self.win_check()
        self.update_player()

    def update_player(self):
        self.currentplayer = self.player1 if self.currentplayer != self.player1 else self.player2

    def win_check(self):
        pass # todo: write win conditions

    def choose_random_player(self):
        choice = random.randint(0, 1)
        self.currentplayer = self.player1 if choice == 0 else self.player2

game = TTTGame()
