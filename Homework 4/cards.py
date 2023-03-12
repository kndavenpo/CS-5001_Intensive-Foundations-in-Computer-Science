'''
    CS5001
    Spring 2022
    Homework 4
    Programming #2: Cards 

    This file includes three commonly used functions for playing cards. The
    first, create_deck(), creates a complete deck of standard playing cards.
    The second, shuffle(), shuffles the deck in a random order. The third,
    deal(), deals up to four hands of cards from the shuffled deck with a max
    of thirteen cards per hand.     
'''

import random 

# Abbreviations for card values and suits
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
SUITS = ['s', 'h', 'd', 'c']

def create_deck( ):
    '''
    Function: create_deck  
    Parameter: None
    Return: a list of cards, not shuffled
    Does: Create a deck of 52 cards with abbreviations for suit and value
    '''

    # Create an empty list for the unshuffled deck 
    unshuffled_deck = []

    # Add all possible combinations of values and suits to the unshuffled deck
    for i in range(len(SUITS)):
        suit = SUITS[i]
        for j in range(len(VALUES)):
            value = VALUES[j]

            card = value + suit
            unshuffled_deck.append(card)

        i += 1
        j += 1

    return unshuffled_deck
        
def shuffle( cards ):
    '''
    Function: shuffle  
    Parameter: a list of cards, not shuffled 
    Return: a list with the cards in a random order (a shuffled deck)
    Does: Shuffle the 52 cards in a new list so that the order is random.
    '''  

    # Get a copy of the unshuffled deck
    unshuffled_deck = create_deck()

    # Take a card in a random location in the unshuffled deck and place it in
    # the shuffled deck until it has all 52 cards.
    i = 0
    shuffled_deck = []   
    for i in range(len(unshuffled_deck)):
        max_random_index = len(unshuffled_deck) - 1
        random_index = random.randint(0, max_random_index)
        random_card = unshuffled_deck[random_index]
        shuffled_deck.append(random_card) 
        unshuffled_deck.pop(random_index)        

    i += 1
    return shuffled_deck
        
def deal( number_of_hands, number_of_cards, cards):
    '''
    Function: deal 
    Parameter:
        number_of_hands (int) - number of hands from 1 to 4
        number_of_cards (int) - number of cards per hand from 0 to 13
        cards (list) - the deck of cards
    Return: a list containing the hands that were dealt
    Does: Deal a max of four hands with a max of 13 cards each. The cards
        dealt should be removed from the deck.
    '''      
    # Create an empty list for the hands 
    hands = []

    # Add the specified number of hands
    for i in range(number_of_hands):
        hand = [] 
        hands.append(hand)

        # Add the specified number of cards for each hand
        for j in range(number_of_cards):
            card = cards[0]
            cards.pop(0)    # Remove the card from the deck
            hand.append(card)  
            j += 1
        i += 1

    return hands   
