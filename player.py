class Player:
    """
    Generates a player with name and balance attributes
    """

    def __init__(self,name,money):
        """
        Initialize the player with name,balance and current bet attributes
        """
        self.name=name
        self.balance=money          #money in hand
        self.bet=0                  #The amount of money the player has bet in the ongoing round
    
    def __str__(self):
        """
        print the player attributes i.e. name and balance
        """
        return "Player {} has {}$ available\n".format(self.name,self.balance)

    def add_money(self,money):
        """
        Add money
        """
        self.balance+=money
        print("Current balance is {}$\n".format(self.balance))

    def remove_money(self,money):
        if(self.balance>=money):
            self.balance-=money
        else:
            print("Insufficient balance!!!")
        print("Current balance is {}$\n".format(self.balance))

#Uncomment the block to test the Class member functions
"""
#Testing
player=Player("xyz",100)
print(player)
player.add_money(30)
player.remove_money(100)
player.remove_money(100)
"""