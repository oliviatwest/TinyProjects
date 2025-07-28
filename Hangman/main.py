import random
import artwork
import wordlist

#logo
print(artwork.logo)

#init variables
chosen_word = random.choice(wordlist.word_list)
lives = 6

placeholder = ""
wordlength = len(chosen_word)

print(chosen_word)
