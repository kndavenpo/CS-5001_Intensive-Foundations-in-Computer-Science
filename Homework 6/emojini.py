"""
    CS5001
    Spring 2022
    Homework 6: Emojini
    Katie Davenport

    This program transforms text into their emoji-based representations and
    back again.
    
"""
from os.path import exists

# Define constants.
DELIMITER = " "
COMMA = ", "    # Added space to help ensure that this is desired punctuation.
PERIOD = ". "   # Added space to help ensure that this is desired punctuation.

def transform_emoji_file(emoji_file_name):
    """
    Function: transform_emoji_file
    Parameter: emoji_file_name (str) - name of the translation mapping file
    Returns: emoji_list (list) - words in each "language"
    Does: Read in emojis file and create a nested list.
    """
    emoji_list = []
    try:
        with open(emoji_file_name, "r", encoding="utf8") as emoji_file:
            translation = []
            for translation in emoji_file:
                translation = translation.split()
                translation[0] = translation[0].lower() 
                emoji_list.append(translation)
    except IOError:
        print("A file error occurred.")
    except OSError:
        print("Error reading file.")    
    return emoji_list                           

def transform_directive_file(directive_file_name):
    """
    Function: transform_directive__file
    Parameter: directive_file_name (str) - name of the directives file
    Returns: directives (list) - contains directives
    Does: Read in directives file and create a nested list.
    """
    
    directives = []
    try:
        with open(directive_file_name, "r") as directive_file:
            for directive in directive_file:
                directive = directive.split(" ")
                directive[3] = directive[3].strip()
                directives.append(directive)
    except IOError:
        print("A file error occurred.")
    except OSError:
        print("Error reading file.")        
    return directives                           

def load_input_text(input_file_name):
    """
    Function: load_input_text
    Parameter: input_file_name (str) - name of input file
    Returns: input_file_text(list) - contains lines of input file
    Does: Read in input file and create list of lines.
    """
    
    input_text = []
    try:
        with open(input_file_name, "r", encoding="utf8") as input_file:
            for lines in input_file:
                line = lines.split(" ")
                input_text.append(line)
    except IOError:
        print("A file error occurred.")
    except OSError:
        print("Error reading file.")        
    return input_text                              

def create_dictionary(emoji_list, from_index, to_index):  
    """
    Function: create_dictionary 
    Parameters:
        emoji_list (list) - words in each "language"
        from_index (int) - the index of the language being translated from
        to_index (int) - the index of the language being translated to
    Returns: A dictionary of words to be translated from (key) and to (value)
    Does: Creates a dictionary of words for translations.
    """
    # Remove first row of metadata.
    emoji_list = emoji_list[1:]
    
    key = []
    for translation in emoji_list:
        # Adjust index for additional word in metadata.
        key_word = translation[from_index - 1] 
        key.append(key_word) 

    value = []
    for translation in emoji_list:
        # Adjust index for additional word in metadata.
        value_word = translation[to_index - 1]
        value.append(value_word)

    temp_dictionary = {}
    for word in range(len(key)):
        temp_dictionary[key[word]] = value[word]
    return temp_dictionary

def save_file(output_file_name, output_text):
    """
    Function: save_file
    Parameters:
        output_file_name (str) - the name of the output file 
        output_text (list) - a list of translated lines 
    Returns: None
    Does: Adds in line break and saves the translated letter to a txt file. 
    """    

    # Add the line break back in.
    for i in range(len(output_text)):
        output_text[i][-1] = output_text[i][-1] + "\n"    

    # Write the file. 
    try:
        with open(output_file_name, "w", encoding="utf8") as output_file:
            for line in output_text:
                line = DELIMITER.join(line)
                output_file.write(line)
    except IOError:
        print("A file error occurred")


def batch_translate(emoji_file_name, directive_file_name): 
    """
    Function: batch_translate
    Parameters:
        emoji_file_name (str) - name of the translation mapping file 
        directive_file_name (str) - name of file with directives 
    Returns: None 
    Does: Executes the translation instructions in the directives file.
    """
    
    # Read in the emojis file and create a nested list.
    emoji_list = transform_emoji_file(emoji_file_name)

    # Read in the directives file and create a nested list.
    directives = transform_directive_file(directive_file_name)

    # Create a table of metadata.  
    metadata = emoji_list[0]
    
    # Execute the directives. 
    for each in directives:

        # Create the temp dictionary. 
        from_index = metadata.index(each[0].upper())
        to_index = metadata.index(each[1].upper())
        temp_dictionary = create_dictionary(emoji_list, from_index, to_index)

        # Read the input file.  
        input_file_name = each[2]
        input_text = load_input_text(input_file_name)
        
        # Translate the text.       
        if len(input_text) > 0:   # Only translate and print if there is text. 
            output_text = []
            for i in range(len(input_text)):
                input_text[i][-1] = input_text[i][-1].strip() 
                line = input_text[i]
                new_words = [] 
                for j in range(len(line)):
                    # Strip punctuation, translate, then add punctuation.
                    if (COMMA in line[j]) or (PERIOD in line[j]):
                        punctuation = line[j][-1]
                        line[j] = line[j].strip(punctuation)
                        if line[j] in temp_dictionary:
                            line[j] = temp_dictionary[line[j]]
                            line[j] = line[j] + punctuation
                            new_words.append(line[j])
                        else:
                            line[j] = line[j] + punctuation
                            new_words.append(line[j])
                    else:
                        if line[j] in temp_dictionary:
                            line[j] = temp_dictionary[line[j]]
                            new_words.append(line[j]) 
                        else:
                            new_words.append(line[j])            
                output_text.append(new_words)

            # Save file and print processing message.
            output_file_name = each[3]
            save_file(output_file_name, output_text) 
            print("Processing " + input_file_name + ": " + each[0] + " -> "
                  + each[1])
  
def main():

    batch_translate('emojis.txt', 'emoji_directives.txt')
    
if __name__ == "__main__":
    main() 
