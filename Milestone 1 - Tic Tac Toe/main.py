from __future__ import print_function
import random
from player import Player
from chessboard import *

class TTTGame:
    board = None
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")
    currentplayer = Player
    game_over = (False, Player)

    def __init__(self):
        self.board = Board()
        self.board.display_board()

        self.choose_random_player()
        self.start()

    def start(self):
        # todo: move logic out into player_choice
        while self.game_over[0] is False:
            print("\nIt is {pl}'s Turn".format(pl=self.currentplayer.playerName))
            player_input = raw_input("Enter a value (1-9): ") # problem suggests using 1-9, but
            adjusted = int(player_input) - 1 # working w/ zero index is easier, so adjustment is made
            if 0 <= adjusted <= 8: # checks between 0/8 but crashes on any other char
                self.place_marker(self.board, self.currentplayer.marker, adjusted)
                self.update_player()
                self.game_over = self.win_check()
            else:
                print("Invalid Selection")

        # todo: insert board-full logic
        print("Congrats to the winner, {pl}".format(pl=self.game_over[1].playerName))
        while self.game_over[0] is True:
            # todo: move out into replay()
            player_input = raw_input("Play again? (y/n) ")
            if player_input == 'y':
                self.game_over = (False, Player)
                self.start()
            elif player_input == 'n':
                print("Play again later!")
            else:
                print("Unknown Selection...\n\n")

    def place_marker(self, board, marker, position):
        row = (position / 3)
        col = position % 3

        if board.update_square(position, self.currentplayer):
            board.display_board()

    def update_player(self):
        self.currentplayer = self.player1 if self.currentplayer != self.player1 else self.player2

    def win_check(self):
        # horiz win conditions
        for row in self.board.return_rows():
            row_owner = row[0].ownedby
            if row_owner != None and row[1].ownedby == row_owner and row[2].ownedby == row_owner:
                print("Row win detected")
                return (True, row_owner)

        # vert win
        for col in self.board.return_cols():
            col_owner = col[0].ownedby
            if col_owner != None and col[1].ownedby == col_owner and col[2].ownedby == col_owner:
                print("Col win detected")
                return  (True, col_owner)

        # diag win
        for line in self.board.return_diag():
            diag_owner = line[0].ownedby
            if diag_owner != None and line[1].ownedby == diag_owner and line[2].ownedby == diag_owner:
                print("Diag win detected")
                return  (True, diag_owner)

        return (False, None)

    def full_board_check(self):
        for row in self.board.return_rows():
            for square in row:
                if square.ownedby == None:
                    return False

        return True

    def choose_random_player(self):
        '''
        Chooses either player 1 or 2 to go first
        
        :return: Player
        '''
        choice = random.randint(1, 11)
        self.currentplayer = self.player1 if choice % 2 == 0 else self.player2


game = TTTGame()
