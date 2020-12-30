from globals import *
from card import Card
import random

class Deck():

    """
    Create a Deck of cards for playing
    """

    def __init__(self):
        """
        Create a deck comprising of all 52 card
        """
        self.deck=[]
        #Iterate over all suits and ranks and append all cards to the deck
        for suit in suits:
            for rank in ranks:
                card=Card(suit,rank)
                self.deck.append(card)
    
    def __str__(self):
        """
        return string to print the entire Deck
        """
        deck_str=""
        for card in self.deck:
            deck_str+=(card.__str__()+"\n")
        return "The deck has {} cards\n".format(len(self.deck))+deck_str

    def shuffle(self):
        """
        Shuffle the deck
        """
        for i in range(len(self.deck)):
            #Pick a random card j from i,i+1,...,len(self.deck)-1
            j=random.randint(i,len(self.deck)-1)
            #Swap cards i & j 
            temp_card=self.deck[i]
            self.deck[i]=self.deck[j]
            self.deck[j]=temp_card

    def draw_card(self):
        """
        If the deck is non-empty,draw a card from it
        """
        if(len(self.deck)>0):
            card=self.deck.pop()
            return card
        else:
            print("The deck is empty can't draw a card")
            return -1

#Uncomment the block to test the Class member functions
"""
#Testing
deck=Deck()
#Shuffle the deck
deck.shuffle()
#Draw 48 cards from the deck
for i in range(48):
    deck.draw_card()
#View the remaining 4 cards
print(deck)
""" 