from card import Card
from deck import Deck
from player import Player
from hand import Hand
from globals import *

"""
High level walkthrough:
1)Make players with their names and initial balance
2)For each game goes on:
    i)Make and shuffle the deck
    ii)Let each player place the bet one by one
    iii)Deal 2 cards each to every player & and the dealer
    iv)Show all cards except a card of the dealer
    v)Go to each player & let him hit until he stands or is busted
    vi)Play the dealer's moves
    vii)Update the balance of each player accordingly
    viii)Print each players balance 
3)After each game ask if they are willing to play another game
4)And if they are willing to play,ask each player if they are willing to add on to their balance
"""

"""
High level function flow :
Players=make_players(num_players)
#here Players is a list of players
place_bet(Players)
deal_cards(Player_hands,dealer_hand)
show_partial(player_hand,dealer_hand)
show_all(player_hand,dealer_hand)
winning=hit_or_stand(Players_hand,dealer_hand)
#winning is a list of either Win,Tie OR Lose for each player
update_balance(Players,winning)
print_balance(Players)
Lets define these functions first
"""

def make_players():
    while(True):
        try:
            num_players=int(input("Give the number of players:"))
            if(num_players<1):
                print("Invalid,the number of players must be positive")
                continue
        except:
            print("Invalid,number of players must be a natural number")
        else:
            break

    Players=[]
    for i in range(num_players):
        print("Player{},get ready!!!\n".format(i+1))
        while(True):
            player_name=input("What's ur name?:")
            if(player_name==""):
                print("Invalid name!!!")
            else:
                break
        while(True):
            try:
                player_money=int(input("How much money are u placing in?:"))
                if(player_money<0):
                    print("Invalid!!!,money placed must be a positive integer")
                    continue
            except:
                print("Invalid!!!,money placed must be a positive integer")
            else:
                break
        print("----------------------------------------------------------------------------")
        player=Player(player_name,player_money)
        Players.append(player)
    return Players

def place_bet(Players):
    for idx,player in enumerate(Players):
        print("Place bet for player{}\n".format(idx+1))
        while(True):
            try:
                player_bet=int(input("How much money are u betting?:"))
                if(player_bet<0 or player_bet>player.balance):
                    print("Invalid!!!,bet must be a positive integer and less than available balance")
                    continue
            except:
                print("Invalid!!!,bet must be a positive integer")
            else:
                break
        player.balance-=player_bet
        player.bet=player_bet
        print("----------------------------------------------------------------------------")
    
def print_bets(Players):
    for player in Players:
        print("{} has placed a bet of {}$\n".format(player.name,player.bet))
    print("----------------------------------------------------------------------------")

def deal_cards(Player_hands,dealer_hand):
    for i in range(2):
        for hand in Player_hands:
            hand.add_card(deck.draw_card())
        dealer_hand.add_card(deck.draw_card())

def show_partial(player_hand,dealer_hand):
    print("DEALER HAND\n")
    print('Card list is:')
    print(dealer_hand.cards[0])
    print("---HIDDEN CARD---\n")
    print("YOUR HAND\n")
    print(player_hand)
    print("------------------------------------------------------------------------------")

def show_all(Player_hands,dealer_hand):
    print("Final dealer hand\n")
    print(dealer_hand)
    for i in range(len(Player_hands)):
        print("Final player{} hand\n".format(i+1))
        print(Player_hands[i])
    print("--------------------------------------------------------------------------")

def hit_or_stand(Player_hands,dealer_hand):
    winning=[]
    while(dealer_hand.value<=16):
        dealer_hand.add_card(deck.draw_card())
    for i,player_hand in enumerate(Player_hands):
        print("Get ready player{}".format(i+1))
        while(True):
            show_partial(player_hand,dealer_hand)
            if(player_hand.value==21):
                print("BLACK JACK!!!")
                break
            while(True):
                cmd=input("Do you want to hit or stand?")
                if(cmd=='h'or cmd=='s'):
                    break
                else:
                    print("Invalid!!!,only 'h' and 's' are valid inputs")
            if(cmd=='h'):
                player_hand.add_card(deck.draw_card())
                if(player_hand.value>21):
                    print("BUSTED!!!")
                    break
                if(player_hand.value==21):
                    print("BLACK JACK!!!")
                    break
            else:
                break
        show_partial(player_hand,dealer_hand)
        if(player_hand.value>21):
            winning.append("Lose")
        elif(dealer_hand.value>21):
            winning.append("Win")
        elif(player_hand.value>dealer_hand.value):
            winning.append("Win")
        elif(player_hand.value==dealer_hand.value):
            winning.append("Tie")
        else:
            winning.append("Lose")
    show_all(Player_hands,dealer_hand)
    #show_winning(winning)
    return winning

def update_balance(Players,winning):
    for idx,player in enumerate(Players):
        if(winning[idx]=="Win"):
            player.balance+=1.5*player.bet
            player.bet=0
        elif(winning[idx]=="Tie"):
            player.balance+=player.bet
            player.bet=0
        else:
            player.bet=0

def print_balance(Players):
    for player in Players:
        print(player)
    print("----------------------------------------------------------------------------")

#MAIN PROGRAM BEGINS :)

play_again=True
Players=make_players()

while(play_again):
    #Print the stating balance in eahc round
    print_balance(Players)

    #Create a new Deck & shuffle it
    deck=Deck()
    deck.shuffle()

    #Initialize player and dealer hands empty
    Player_hands=[]
    for i in range(len(Players)):
        Player_hands.append(Hand())
    dealer_hand=Hand()

    #Let each player place bets
    place_bet(Players)
    print_bets(Players)
    print_balance(Players)

    #deal cards to each player & the dealer
    deal_cards(Player_hands,dealer_hand)

    #Allow each player to HIT or STAND & check if they win,tie or lose
    winning=hit_or_stand(Player_hands,dealer_hand)

    #Update the balance of each depending on whether it was a win,tie or lose
    update_balance(Players,winning)

    #Print out the balance of each player
    print_balance(Players)

    #Asks if they wanna play another game
    while(True):
        cmd=input("Want to play another round y/n:")
        if(cmd=='y'or cmd=='n'):
            if(cmd=='n'):
                print("Thanks for playing!!!")
                play_again=False
            break
        else:
            print("Invalid!!!,input should be y or n only")
