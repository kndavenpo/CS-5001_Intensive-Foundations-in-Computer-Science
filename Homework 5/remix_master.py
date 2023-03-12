"""
    CS5001
    Spring 2022
    Homework 5: Remix Master
    Katie Davenport

    This program allows users to remix a song. The user is able to select and
    load a song to remix, substitute an existing word in the song with a new
    word, reverse the order of the words in each line, play back the remixed
    song, and reset the song's lyrics to their original version.         
"""

from music import PLAYLIST, SONGS

# Define constants used in the program  
MAIN_MENU_CHOICES = ["L", "T", "S", "P", "R", "X", "Q"]
MUSIC_NOTES = "-♫"
PUNCTUATION = ".?!:,"
DELIMITER = " "

def choose_menu(): 
    """
    Function: choose_menu
    Parameters: none
    Returns: choice(string) - the user's choice of action
    Does: Allows a user to select an action from a menu.
    """
    
    print("\nRemix-Master:\n"
          "L: Load a different song\n"      
          "T: Title of current song\n"
          "S: Substitute a word\n"
          "P: Playback your song\n"
          "R: Reverse it!\n"
          "X: Reset to original song\n"
          "Q: Quit?\n")
    choice = input("Your choice: ")
    choice = choice.upper()
    return choice


def choose_song_menu(): 
    """
    Function: choose_song_menu
    Parameters: none
    Returns: choice(integer) - the user's song choice
    Does: Allows a user to select a song from a menu.
    """

    print("Choose the number for song you want to load: ")   
    for i in range(len(PLAYLIST)):
        print(str(i + 1) + ":", PLAYLIST[i]) 
    choice = input("\nYour choice: ")

    # Defensive programming to require valid inputs
    while choice.isdigit() is False or int(choice) not in [1, 2, 3]: 
        choice = input("Enter a valid number please: ")
      
    choice = int(choice)
    return choice

    
def load_song(choice):    
    """
    Function: load_song
    Parameter: choice(integer) - the user's song choice 
    Return: loaded_song (list) - the selected song's lyrics and title 
    Does: Loads the song lyrics and title if the selection is valid. 
    """

    song_choice_index = choice - 1
    if int(choice) <= len(PLAYLIST) and int(choice) > 0:
        loaded_song = [SONGS[song_choice_index], PLAYLIST[song_choice_index]]

    # Extraneous due to defensive programming in choose_song_menu
    else:
        print("Invalid choice. Mix song unchanged.")
        loaded_song = []
    return loaded_song


def substitute(song, old_word, new_word): 
    """
    Function: substitute
    Parameters:
        song (list) - each line of a song's lyrics
        old_word (string) - an existing word in the song
        new_word (string) - a replacement word
    Return: replace (boolean) - true if replacement is successful else false
    Does: Replaces an old word with a new word and removes punctuation if the
    old word is in the song. 
    """
    
    words = DELIMITER.join(song) 
    old_word_count = words.count(old_word)
    
    if old_word_count != 0:                         
        for i in range(len(song)):
            line = song[i]                          
            line_list = line.split(DELIMITER)
            for j in range(len(line_list)):
                line_list[j] = line_list[j].strip(PUNCTUATION)
                if line_list[j] == old_word:
                    line_list[j] = new_word    
                line_list_new_word = DELIMITER.join(line_list)
            song[i] = line_list_new_word    
        replace = True
    else:     
        print(f"Sorry. I didn't find {old_word} in the existing song.")
        replace = False

    return replace                   


def reverse_it(song):
    """
    Function: reverse_it
    Parameter: song (list) - each line of a song's lyrics
    Return: song (list) - each line of the song's lyrics reversed
    Does: Reverses the order of the words in a song and removes punctuation. 
    """

    for i in range(len(song)):
        line = song[i]          
        line_list = line.split(DELIMITER)
        for j in range(len(line_list)):
            line_list[j] = line_list[j].strip(PUNCTUATION)
        line_list = line_list[::-1]
        line_list = DELIMITER.join(line_list)
        song[i] = line_list

    return song


def main():

    # Set a default song to the first song in the playlist. 
    loaded_song = SONGS[0]
    title = PLAYLIST[0]
    loaded_song_copy = loaded_song.copy()
    song_choice = 1                           

    # Drives the program based on the user's selected action.
    done = False
    while not done:
        option = choose_menu()
        if option == "L":                            
            song_choice = choose_song_menu()        
            loaded_song_list = load_song(song_choice)
            loaded_song = loaded_song_list[0]
            title = loaded_song_list[1]
            loaded_song_copy = loaded_song.copy()  
        elif option == "T":                         
            print(MUSIC_NOTES * 20)
            print("You are mixing the song:", title)  
        elif option == "S":     
            song = loaded_song_copy  
            old_word = input("What word do you want to replace in the \
existing song? ").lower()
            new_word = input("What new word do you want to use for the song? \
").lower()                   
            substitute(song, old_word, new_word)
        elif option == "R":
            song = loaded_song_copy
            reverse_it(song)
        elif option == "X":                         
            loaded_song_copy = loaded_song.copy()
        elif option == "P":                         
            print("Turn up the 808's and drop the beat! Here's your remix:")
            for i in range(len(loaded_song_copy)):
                print(loaded_song_copy[i])
            print(MUSIC_NOTES * 20)    
        elif option not in MAIN_MENU_CHOICES:
            print("Invalid choice. Mixed song unchanged")
        elif option == "Q":
            done = True 
 
    print("Bravo! Your Grammy Award is being shipped to you now!")
    
if __name__ == "__main__":
    main() 
