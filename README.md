# BotMacklin
### Discord Bot for personal use 

## Main Uses 
* Sending gifs and messages in response to calling set commands in Discord chat 
* Wordle Wrecker (See Below) through DM's

## Wordle Wrecker 
* Analyzes English Dictionary to help figure out most likely words (based on placement of letters and clues already revealed)
* When finding matches, it will find probabilies of letters being in some place (i.e. the letter r being the second letter), and then find the most likely words based on that. I'm not using any sort of usage frequency, since I don't want common words to dominate suggestions (I don't think common words should have any pull). I might give them some weight in the future.

#### Wordle Help Input 
* Input had two main parts, which is set up because there is currently nothing to keep unique sessions going between users for help (if being used through BotMacklin) 
* Formatting: 
    - *****: 5 empty slots, no hints 
    - Lowercase letters: letter is in the word, place is unknown (Yellow)
    - Uppercase letters: letter is in the word and in the correct place (Green)
    - After the five letters, you can include a ',' followed by all the letters which are not in use (Grey) 

## Setup Instructions 
To come later 
