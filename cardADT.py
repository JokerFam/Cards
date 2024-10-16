# cardADT.py
# Module file implementing the card ADT with functions

_SUITS = 'cdhs'
_SUITS_NAMES = ['clubs', 'diamonds', 'hearts', 'spades']
_RANKS = range(1,14)
_RANK_NAMES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
                'Eight', 'nine', 'Ten', 'Jack', 'Queen', 'king']

def create(rank, suit):
    assert rank in _RANKS and suit in _SUITS
    return (rank, suit)

def rank(card):
    return card[0]

def suit(card):
    return card[1]

def suitName(card):
    index = _SUITS.index(suit(card))
    return _SUITS_NAMES[index]

def rankName(card):
    index = _RANKS.index(rank(card))
    return _RANK_NAMES[index]

def toString(card):
    return rankName(card) + ' of ' + suitName(card)