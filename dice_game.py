# dice_game.py

from random import randint

sides = input("Enter dice sides: ")
sides = int(sides)

player1_name = input("Enter player1 name: ")
player2_name = input("Enter player2 name: ")

player1_wins = 0
player2_wins = 0

total_turns = 11
current_turn = 1

while current_turn <= total_turns:
    player1_dice_roll = randint(1, sides)
    player2_dice_roll = randint(1, sides)

    print(player1_name + " rolled: " + str(player1_dice_roll))
    print(player2_name + " rolled: " + str(player2_dice_roll))

    if player1_dice_roll > player2_dice_roll:
        player1_wins = player1_wins + 1
    else:
        player2_wins = player2_wins + 1

    current_turn += 1

if player1_wins > player2_wins:
    print(player1_name + " wins!")
else:
    print(player2_name + " wins!")
    
