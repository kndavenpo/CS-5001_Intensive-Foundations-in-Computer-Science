'''
    CS5001
    Spring 2022
    Homework 3
    Programming #3: Pokemon Tournament 
    A program that runs a Pokemon tournament for Rocks-Paper-Scissors (RPS).
'''

import random

def get_player( number ):
    '''
    Function: get_player  
    Parameter: number (int) - an integer corresponding to a Pokemon player  
    Return: player (string) - the name of the player 
    Does: Returns the name of a player associated with the numbering scheme.
    '''  
    if number == 1:
        player = 'Bulbasaur'
    elif number == 2:
        player = 'Charmander'
    elif number == 3:
        player = 'Butterfree'  
    elif number == 4:
        player = 'Rattata'
    elif number == 5:
        player = 'Weedle'  
    elif number == 6:
        player = 'Pikachu'
    elif number == 7:
        player = 'Sandslash'
    elif number == 8:
        player = 'Jigglypuff'
    elif number == 9:
        player = 'Raichu'
    else:
        player = 'Diglett'

    return player
    
def check_battle( computer, player ):
    '''
    Function: check_battle 
    Parameter:
        computer (int) - the number for the computer's RPS selection
        player (int) - the number for the player's RPS selection 
    Return: result (string) - the outcome of the game 
    Does: Determines winner based on the RPS selections.
    '''  
    if computer == player:
        result = 'DRAW!'
    elif (computer == 1 and player == 3) or (computer == 2 and player == 1) or\
         (computer == 3 and player == 2):
        result = 'COMPUTER'
    else:
        result = 'PLAYER'

    return result 

def get_rps( number ):
    '''
    Function: get_rps 
    Parameter: number (int) - the integer associated with the RPS value
    Return: choice (string) - the RPS value 
    Does: Converts the RPS number to the RPS string value.
    '''  
    if number == 1:
        choice = 'ROCK'
    elif number == 2:
        choice = 'PAPER'
    elif number == 3:
        choice = 'SCISSORS'  

    return choice
   
 
def main():

    # Assign teams based on user input
    player_team = input('What team do you want (red or blue)? ')
    player_team = player_team.upper() # convert to uppercase for consistency
 
    if player_team == 'RED':
        computer_team = 'BLUE'
    else:
        player_team = 'BLUE'
        computer_team = 'RED'

    # Define variables needed to quit the game and calculate win counts
    play_again = ''
    player_counter = 0
    computer_counter = 0

    # Create the while loop that allows the user to replay and quit
    while play_again != 'N':
        
        # Assign player and computer Pokemon
        player_pokemon = get_player(random.randint(1, 10))
        computer_pokemon = get_player(random.randint(1, 10))

        # Input the player's RPS number
        print(f'{player_team} {player_pokemon} vs. {computer_team} \
{computer_pokemon}')
        player_number = int(input('Enter 1 for Rock, 2 for Paper, \
3 for Scissors '))

        # Assign a random RPS number to computer
        computer_number = (random.randint(1, 3))

        # Convert RPS number to string for player and computer 
        player_object = get_rps(player_number)
        computer_object = get_rps(computer_number)

        # Get winner
        winner = check_battle( computer_number, player_number )

        # Print result
        print(f'{player_pokemon} played {player_object}. {computer_pokemon} \
played {computer_object}')
    
        # Get winner
        winner = check_battle( computer_number, player_number)

        if winner == 'PLAYER':
            print(f'Your {player_team} wins with {player_pokemon}!\n')
            player_counter += 1
            
        if winner == 'COMPUTER':
            print(f'My {computer_team} wins with {computer_pokemon}!\n')
            computer_counter += 1

        if winner == 'DRAW!':
            print(f'It is a draw! No winner\n')

        # Give the player the option to play again or quit
        play_again = input('play again (y/n)? ')
        play_again = play_again.upper() # convert to uppercase for consistency

        # Print final results if the player quits
        if play_again == 'N':
            print('Tournament has ended!')
            print(f'{player_team}:{player_counter}  \
{computer_team}:{computer_counter}')
            if computer_counter > player_counter:
                print('I WIN!!!')
            elif computer_counter < player_counter:
                print('YOU WIN ... UNTIL NEXT TIME!!!')
            else:
                print('WE TIED!')

if __name__ == "__main__":
    main()
