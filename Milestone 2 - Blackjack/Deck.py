from PlayingCard import PlayingCard
from encodings import latin_1

class Deck(object):
    _suits = ["\u2663".encode('ascii'), "\u2660", "\u2665", "\u2666"]
    _card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    _numberOfDecks = -1
    _decks = []

    def __init__(self, number_of_decks):
        self._numberOfDecks = number_of_decks

        self._decks += [self.__create_deck_() * self._numberOfDecks]

    def __create_deck_(self):
        return_deck = []
        for s in self._suits:
            for c in self._card:
                return_deck.append(PlayingCard(s, c))
        return return_deck

    def display_decks(self):
        for deck in self._decks:
            for card in deck:
                print card
