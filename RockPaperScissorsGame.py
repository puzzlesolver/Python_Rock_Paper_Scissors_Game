import random

# Global counter variables to store total number of wins
computer_wins = 0
human_wins = 0

# Function for the user to choose rock, paper, or scissors as an option.
# This function contains an array of strings for the user to choose from,
# as well as conditions that allows the fucntion to return the selected value.
def human():
    human_choice = input('Choose Rock, Paper, or Scissors: ')
    choices = ['r', 'p', 's']
    if human_choice in choices[0]:
        human_choice = 'r'
    elif human_choice in choices[1]:
        human_choice = 'p'
    elif human_choice in choices[2]:
        human_choice = 's'
    else:
        print('Valid options are only: r, p, or s. Please use only these options to play the game.')
        human()
    return human_choice

# Fuction for the program to randomly select rock, paper, or scissors from the string array.
def computer():
    select = ['r', 'p', 's']
    computer_choice = random.choice(select)

    return computer_choice

while True:
    human_choice = human()
    computer_choice = computer()

    if human_choice == 'r':
        if computer_choice == 'r':
            print('You chose rock. The computer chose rock. You tied.')
        elif computer_choice == 'p':
            print('You chose rock. The computer chose paper. You lose.')
            computer_wins += 1
        elif computer_choice == 's':
            print('You chose rock. The computer chose scissors. You win.')
            human_wins += 1

    elif human_choice == 'p':
        if computer_choice == 'r':
            print('You chose paper. The computer chose rock. You win.')
            human_wins += 1
        elif computer_choice == 'p':
            print('You chose paper. The computer chose paper. You tied.')
        elif computer_choice == 's':
            print('You chose paper. The computer chose scissors. You lose.')
            computer_wins += 1

    elif human_choice == 's':
        if computer_choice == 'r':
            print('You chose scissors. The computer chose rock. You lose.')
            computer_wins += 1
        elif computer_choice == 'p':
            print('You chose scissors. The computer chose paper. You win.')
            human_wins += 1
        elif computer_choice == 's':
            print('You chose scissors. The computer chose scissors. You tied.')

    print('Human number of total wins: ' + str(human_wins))
    print('Computer number of total wins: ' + str(computer_wins))

    human_choice = input('Do you want to play again? (y/n)')
    affirmative = ['Y', 'y']
    negative = ['N', 'n']
    if human_choice in affirmative:
        pass
    elif human_choice in negative:
        break
    else:
        break







