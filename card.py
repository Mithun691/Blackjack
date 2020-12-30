from globals import *

class Card():

    """
    Create a card of a particular suit,rank and value
    """

    def __init__(self,suit,rank):
        """
        Initialize a Card object with its suit,rank and value attributes
        """
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        """
        return string suggesting the format to print the Card object 
        """
        return "{} of {}".format(self.rank,self.suit)

#Uncomment the block to test the Class member functions
"""
#Testing 
card=Card("Spade","king")       #create and initialize a Card object
print(card)                     #print the Card attributes
"""