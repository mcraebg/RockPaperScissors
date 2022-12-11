import random

rock = "Rock"
paper = 'Paper'
scissors = "Scissors"
computer_move = ''
computer_score = 0
player_score = 0
while True:
    player_move = input("\nChoose [r]ock, [p]aper, [s]cissors or [e]nd: ")
    if player_move == "r":
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    elif player_move == 'e':
        break
    else:
        print("\nInvalid Input. Try again...")
        continue
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = rock
    elif random_number == 2:
        computer_move = paper
    elif random_number == 3:
        computer_move = scissors
    print(f'The computer choice is: {computer_move}')
    if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
        player_score += 1
        print('\nYou win!')
    elif player_move == computer_move:
        print("\nDraw!")
    else:
        computer_score += 1
        print("\nYou lose!")
    print(f'\nPlayer score: {player_score}   Computer score: {computer_score}')
if computer_score > player_score:
    print('\nCOMPUTER WINS!')
elif computer_score == player_score:
    print('\nDRAW!')
else:
    print('\nPLAYER WINS!')