import random

#art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]


def playgame():
#player input 
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#display user input 
    if user_choice >= 0 and user_choice <= 2:
        print(game_images[user_choice])

#computer choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

#determine winner
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number. You lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")

#welcome message
print("Welcome to Rock, Paper, Scissors! Let's play!")

playgame()

#ask to play again
playagain = input("Do you want to go again? Type 'yes' or 'no'. \n")
while playagain.lower() == 'yes':
    playgame()
    playagain = input("Do you want to go again? Type 'yes' or 'no'. \n")

