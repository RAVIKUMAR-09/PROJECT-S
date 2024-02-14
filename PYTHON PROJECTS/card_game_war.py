# For this project you will be using OOP create a card game. This card game will
# be the card game "war" for two players,You an the computer.If you don,t know
# how to play "war" here are basic rules:
#
# The deck is divided evenly,with each player receving 26 cards,dealt one at a time,
# face down.Anyone may deal first,Each places his stack of cards face down,
# in front of him.
#
# The play:
#
# Each player turns a card at the same time and the palyer with the higher card
# takes both cards and puts them, face down,an the bottom of his stack.
#
# If the cards are the same rank, it is war.Each player turns us three cards fcae
# down and one card face up. The palyer with the higher cards takes both piles
# (six crads.) if the turned-up cards are agian the same rank ,eack player places
# another  card face down and turns another card face up, The palyer with the 
# higher card takes all 10 cards, amd so on.
# 
# There are some more variations on this we will keep ii simple fpr now.
#
# https://en.wekipedia.org/wiki/War (card_game)

from random import shuffle

# Two useful variables for creating Cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

mycard = '[(s,r) for s SUITE for r in RANKS]'

# macards = []
# for r in RANKS:
#     for s in SUITE:
#         mycard.append((s,r))

class Deck:
    """
    This is the Deck Class.This object will create a deck of cards to initiate paly.
    You can then use this Deck list pf cards to spilt in half and give to the players.
    It will use SUTE and RANKS to create the deck. It should also have a method for
    splitting/cutting the deck in half and Shuffling the deck. 
    
    """
    def __init__(self):
        print("Creating New Ordered Deck!")
        #self.allcards =  [(s,r) for s SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])

class HAND:
    '''
    This is the hand. Each player has a Hand, and can add or remove
    caeds form that hand.There should be an add remove card method here.
    '''

    def __init__(self , cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
    
    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the player class,which takes in a name and an intances pf a hand class 
    object. The palyer can then play cards and check if they still have cards.

    """
    
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}" .format(self.mame,drawn_card))
        print("\n")
        return drawn_card
    
    def remove_war_cards(self):
        war_card = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_card.append(self.hand.remove_card())
            return war_card
    
    def still_has_cards(self):

        #Return True if palyer still has cards left

        return len(self.hands.cards) != 0
    

#############################################################################################

######################################  GAME PLAY    ########################################

#############################################################################################

print("Welocome to war , let's begin")

# Create new deck and split it in half

d  = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

# create both player

comp = 'Player("computer", Hand(ha1f1))'

name = input("what is your name?")
user = 'player(name,Hand(half2))'

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("here are the current standings")
    print(user.name+ "has the count:" +str(len(user.hand.cards)))
    print(comp.name+ "has the count:" +str(len(comp.hand.cards)))
    print("play a card!")
    print('\n')


    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()


    table_cards.append(c_card)
    table_cards.append(p_card)
    

    if c_card[1] == p_card[1]:
        war_count += 1

        print("war !")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("Game over,number of rounds :+str(total_rounds)")
print("a war happend "+str(war_count)+"times")


# use the 3 clasees along with logic to play a game of war !

        