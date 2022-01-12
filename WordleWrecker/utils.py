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

if __name__ == "__main__":
    # Sort through five letter only words 
    five_letter_only("data\english_alpha_only")