# Card.py

class Card(object):
    """
    A simple playing card. A card is characterized by two components.
    rank: An integer value in the range 1-13, inclusive (Ace-King)
    suit: a character in 'cdhs' for clubs, diamonds, hearts, and spades
    """

    SUITS = 'cdhs'
    SUIT_NAMES =  ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    RANKS = range(1,14)
    RANK_NAMES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                    'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

    def __init__(self, rank, suit) -> None:
        """
        Constructor
        pre: range in range (1,14) and suit in 'cdhs'
        post: self has the given rank and suit
        """
        self.rank_num = rank
        self.suit_char = suit

    def suit(self):
        """
        Card suit
        post: Returns the suit of self as a single character
        """
        return self.suit_char

    def rank(self):
        """
        Card rank
        post: Returns the rank of self as an int
        """
        return self.rank_num

    def suitName(self):
        """
        Card suit name
        post: Return one of ('Clubs', 'Diamonds', 'Heart', 'Spades') corresponding to self's suit.
        """
        index = self.SUITS.index(self.suit_char)
        return self.SUIT_NAMES[index]
    
    def rankName(self):
        """
        Card rank name
        post: Returns one of ('Ace', 'Two', 'Three', ..., 'King') corresponding to self's rank
        """
        index = self.RANKS.index(self.rank_num)
        return self.RANK_NAMES[index]

    def __str__(self):
        """
        String representation
        post: Returns string representating self, e.g 'Ace of Spades'
        """
        return self.rankName() + ' of ' + self.suitName()