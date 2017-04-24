class PlayingCard(object):

    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "{v}{s}".format(v=self.value, s=self.suit)
        # return "%s%s" % (self.value, self.suit)