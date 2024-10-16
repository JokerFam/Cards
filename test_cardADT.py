# test_cardADT.py
from cardADT import *

def printAll():
    for s in 'cdhs':
        for r in range(1,14):
            card = create(r,s)
            print ('Suit: ', suit(card))
            print ('Rank: ', rank(card))
            print (toString(card))

if __name__ == '__main__':
    printAll()