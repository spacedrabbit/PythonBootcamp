import Deck

class Blackjack(object):

    def __init__(self):
        self.start()

    def start(self):

        deck = Deck.Deck(1)
        deck.display_decks()


Blackjack().start()