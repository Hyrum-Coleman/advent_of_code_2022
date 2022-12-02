# Hyrum Coleman
# Advent of Code Day 2

import csv

# 1. Read input from rock_paper_scissors_input.csv

with open('rock_paper_scissors_input.csv', 'r') as f:
    reader = csv.reader(f)
    input_list = list(reader)

user_score = 0
computer_choice = 'null'
player_choice = 'null'

for _, item in enumerate(input_list):

    for _, character in enumerate(item[0]):

        if character == ' ':
            pass
        elif character == 'A':
            computer_choice = 'r'
        elif character == 'B':
            computer_choice = 'p'
        elif character == 'C':
            computer_choice = 's'
        elif character == 'X':
            player_choice = 'r'
            user_score += 1
        elif character == 'Y':
            player_choice = 'p'
            user_score += 2
        elif character == 'Z':
            user_score += 3
            player_choice = 's'
        else:
            raise ValueError('Invalid input')

    if player_choice == computer_choice:
        print(f"Both players selected {player_choice}. It's a tie!")
        user_score += 3
    elif player_choice is 'r':
        if computer_choice is 's':
            print("The player wins, rock smashes scissors\n")
            user_score += 6
        else:
            print("The computer wins, paper covers rock\n")
    elif player_choice is 'p':
        if computer_choice is 'r':
            print("The player wins, paper covers rock\n")
            user_score += 6
        else:
            print("The computer wins, scissors cuts paper\n")
    elif player_choice is 's':
        if computer_choice is 'p':
            print("The player wins, scissors cuts paper\n")
            user_score += 6
        else:
            print("The computer wins, rock smashes scissors\n")
    else:
        raise ValueError('Fucked around and found out')

print(user_score)
