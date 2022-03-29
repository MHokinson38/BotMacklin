#########################
# Utils file for random faff
#########################

def five_letter_only(data_file):
    with open("data\\five_letter_words.txt", "w") as out_f:
        with open(data_file, "r") as english_words:
            word_list = english_words.readlines()

            for word in word_list:
                if len(word) == 6:      # There is a newline character still included apparently 
                    out_f.write(word)

def get_five_unique_words():
    letters_so_far = set()
    word_list = []

    with open("data/five_letter_words.txt", "r") as out_f:
        full_word_list = out_f.readlines()

    curr_word_idx = 0   # 10222
    word_indices = {}
    highest_letter = ''
    while (len(word_list) < 5):
        curr_word = full_word_list[curr_word_idx][:-1]

        # Check first letter 
        if highest_letter > curr_word[0]:
            removed = word_list.pop()
            curr_word_idx = word_indices[removed] + 1# Backtracking 
            for letter in removed:
                letters_so_far.remove(letter)

            highest_letter = '' if len(letters_so_far) == 0  else max(letters_so_far)
            
            continue

        unique = True
        temp_list = set()
        for letter in curr_word:
            if letter in letters_so_far or letter in temp_list:
                unique = False
                break
            temp_list.add(letter)

        if unique:
            word_indices[curr_word] = curr_word_idx
            word_list.append(curr_word)

            letters_so_far = letters_so_far.union(temp_list)

            highest_letter = max(highest_letter, max(temp_list))

        print(f"{word_list}, with current idx: {curr_word_idx}")

        if curr_word_idx == len(full_word_list) - 1:
            while curr_word_idx == len(full_word_list) - 1:
                if len(word_list) == 0:
                    print("No Combinations")
                    return 

                removed = word_list.pop()
                curr_word_idx = word_indices[removed] # Backtracking 
                for letter in removed:
                    letters_so_far.remove(letter)

            highest_letter = '' if len(letters_so_far) == 0  else max(letters_so_far)

        curr_word_idx += 1
    

if __name__ == "__main__":
    # Sort through five letter only words 
    get_five_unique_words()