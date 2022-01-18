############################
# Wordle Help Program 

## Input format and other usage can be seen in the README file in the BotMacklin Directory 
############################
import numpy as np

# Constants 
FIVE_LETTER_WORDS_PATH = 'data\\five_letter_words.txt'
TOTAL_WORD_COUNT = 15918                                # line count for above text file 

UPPER_CASE_LETTERS = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
LOWER_CASE_LETTERS = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}

# Generate a frequencey model of (letter, place(0->4)) => count 
# The idea is to find the most likely places for each letter 
# This model is going to be used for the unknown letters, then we will set up backtracking 
# find words which best fit this model, since those should be a better next guess 
def generate_model(word_list):
    model = {}
    for word in word_list:
        for idx, letter in enumerate(word):
            model[(letter, idx)] = model.get((letter, idx), 0) + 1

    for key, value in model.items(): 
        model[key] = 1.0 * value / TOTAL_WORD_COUNT

    return model

# Goes through the current word list (all the 5 letter words), and patter matches to find 
# word_clue is the string with the known places
# white_list is all of the letters which we know should be in the word (with and without known placement)
# black_list is all of the letters which we know are not in the word 
def sort_through_clues(word_list, word_clue, white_list, black_list):
    sorted_list = []

    for word in word_list:
        # Check the black list for matches 
        # matching all letters in word are not in black_list (if any are, then we skip the word)
        if black_list is not None:
            matched_black_list = [letters in black_list for letters in word]
            if any(matched_black_list):
                continue

        # Check for containing all of the letters word_clue which we know should be there 
        # match that all letters in white list are in the word (all(list) should return true)
        if white_list is not None:
            matched_white_list = [letters in word for letters in white_list]
            if not all(matched_white_list):
                continue

            # Check indices to make sure they haven't been checked already 
            index_mismatch = False
            for idx, letter in enumerate(word):
                if letter in white_list and idx in white_list[letter]:
                    index_mismatch = True
                    break
            if index_mismatch:
                continue

        # Match the known placements 
        pattern_matched = True 
        for idx, clue in enumerate(word_clue):
            if clue != '*' and clue != word[idx]:     # not matching with required letter 
                pattern_matched = False
                break
        
        if pattern_matched:
            sorted_list.append(word)

    return sorted_list

def rank_matches(model, matched_words, count):
    words_and_probs = {}

    for word in matched_words:
        prob = 0
        for idx, letter in enumerate(word):
            prob += np.log(model[(letter, idx)])

        words_and_probs[word] = prob
    
    # sort and return the most likely (top matched_words)
    sorted_words = [(key, value) for key, value in sorted(words_and_probs.items(), key=lambda x: x[1], reverse=True)]
    return sorted_words[:count]

# Parses the input string, creating the black_list, white_list, and clue strings 
# Keeps runnign white list for better guessing, but that requires a runnign session 
def parse_input(input_string, white_list, black_list):
    splits = input_string.split(',')

    if len(splits) > 2 or len(splits[0]) != 5:
        raise ValueError("Input clue string is not formatted properly")

    clue = splits[0]
    if black_list is None:
        black_list = set(splits[1].lower()) if len(splits) == 2 else None
    else:
        black_list = black_list.union(set(splits[1].lower()))

    if white_list is None:
        white_list = {}

    clue_string = ""
    for idx, letter in enumerate(clue):
        if letter in UPPER_CASE_LETTERS:
            letter = letter.lower()
            clue_string += letter
            white_list[letter] = white_list.get(letter, set())
        elif letter in LOWER_CASE_LETTERS:
            white_list[letter] = white_list.get(letter, set())
            white_list[letter].add(idx)     # Stores letters we need, but the indices they are not at 
            clue_string += '*'
        else:
            clue_string += '*'

    return clue_string, white_list if len(white_list) > 0 else None, black_list

if __name__ == '__main__':
    white_list = None
    black_list = None
    while(True):
        input_string = input(f"Enter the input string: ")

        clue_string, white_list, black_list = parse_input(input_string, white_list, black_list)

        print(f"Parsed input. Clue: {clue_string}, White List: {white_list}, Black List: {black_list}")

        with open(FIVE_LETTER_WORDS_PATH, "r") as word_list_f:
            word_list = word_list_f.readlines()
            word_list = [word[:-1] for word in word_list]

        model = generate_model(word_list)
        matches = sort_through_clues(word_list, clue_string, white_list, black_list)
        best_matches = rank_matches(model, matches, 10)
        
        print(f"The best 10 words: {best_matches}")
