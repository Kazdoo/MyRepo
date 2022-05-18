# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:02:14 2022

cards


@author: oged
"""
from __future__ import print_function, division
import random

class Card:
    """represent a standard playing card."""
    def __init__(self,suit=0,rank=2):
        self.suit = suit
        self.rank = rank
        
    suit_names = ['Clubs','Diamonds', 'Hearts', 'Spades']
    rank_names = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        """Compares this card to other, first by suit, then rank.
        returns: boolean
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    

    def __eq__(self, other):
        """Checks whether self and other have the same rank and suit.
        returns: boolean
        """
        return self.suit == other.suit and self.rank == other.rank


class Deck:
    
    #creating a list of all 52 cards
    def __init__(self):
        self.cards =[]
        for suit in range (4):
            for rank in range (1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    #build in function str to print something.
    def __str__(self): 
        res = []
        for card in self.cards:
            res.append (str(card))
        return '\n'.join(res)
    
    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)
    
    
    def add_card(self, card):
        self.cards.append(card)
        
    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)
        
    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()
        
    def move_cards (self, hand, num):    
        for i in range (num):
            hand.add_card(self.pop_card)
            
        
    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there.
        
        card: Card
        """
        self.cards.remove(card)
        
            
class Hand(Deck):
    "represent a hand of playing cards."
    def __init__ (self, label=''):
        self.cards = []
        self.label = label
        
def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.
    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None
        
if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    #hand.sort()
    print(hand)
        