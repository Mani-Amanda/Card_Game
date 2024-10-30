from random import shuffle


class Card:
    suits = ["spades", #define cards
             "hearts",
             "diamonds",
             "clubs"]

    values = [None, None,"2", "3", #values of cards
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):   #suit
        """suit + value are ints"""
        self.value = v
        self.suit = s