import random
import artwork
import wordlist


#init variables
chosen_word = random.choice(wordlist.word_list)
lives = 6
game_over = False


placeholder = ""
wordlength = len(chosen_word)
correct_guesses = []




#logo and game start
print(artwork.logo + "\n")



#establish placeholder for blanks and letters
for position in range(wordlength):
    placeholder += "_"

print("Ready? Here's your word: " + placeholder + "\n")
print (chosen_word)

while not game_over: 

    print("******You have " + str(lives) + " lives left!******\n")

    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in correct_guesses:
        print("You already guessed that letter. Try again.\n")
    


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    print("Current word: " + display + "\n")

    if guess not in chosen_word:
        lives -= 1
        print("You guessed " + guess + ", which is not in the word. You lose a life.\n")

        if lives == 0:
            game_over = True
            print("******You lose! The word was: " + chosen_word + "******")
    
        
    if "_" not in display:
        game_over = True
        print("******Congratulations! You guessed the word: " + chosen_word + "******")

    print(artwork.stages[lives])



