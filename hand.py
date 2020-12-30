from card import Card

class Hand():
    """
    generate the hand for dealer and players
    """

    def __init__(self):
        """
        Create an empty hand
        """
        self.cards=[]
        self.value=0            #Optimal value of hand
        self.ace_count=0        #Number of aces count as 11 presently

    def __str__(self):
        """
        return string to print the hand
        """
        cards_in_hand='Card list is:\n'
        for i in range(len(self.cards)):
            cards_in_hand+=self.cards[i].__str__()+"\n"
        
        return "This hand has a value of {}.\n\n".format(self.value) + cards_in_hand

    def add_card(self,card):
        """
        Add a card to the hand & maximise value keeping it <= 21
        """
        self.cards.append(card)
        self.value+=card.value

        if(card.rank=="ace"):
            self.ace_count+=1
        #Try decreasing the value to <=21 by evaluating ace as 1 instead of 11
        while(self.value>21 and self.ace_count>0):
            self.value-=10
            self.ace_count-=1

#Uncomment the block to test the Class member functions
"""
#Testing
hand=Hand()
card1=Card("Club","ace")
card2=Card("Heart","seven")
card3=Card("spade","ace")
hand.add_card(card1)
print(hand)
hand.add_card(card2)
print(hand)
hand.add_card(card3)
print(hand)
"""