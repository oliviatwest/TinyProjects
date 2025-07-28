import random
import artwork
import wordlist

#logo
print(artwork.logo + "\n")


#init variables
chosen_word = random.choice(wordlist.word_list)
lives = 6
game_over = False


placeholder = ""
wordlength = len(chosen_word)

for position in range(wordlength):
    placeholder += "_"
print("Ready? \n" + "Here's your word: " + placeholder)
