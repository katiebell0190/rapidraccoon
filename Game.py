import random
print('Welcome to Rock, Paper, Scissors')

while True:
    options = ["rock", "paper", "scissors"]
    player = input("rock, paper or scissors? ")
    computer = random.choice(options)
    print (f"\nPlayer 1 chose {player}, the machine chose {computer}.\n")

    if player == computer:
            print(f"Both players selected {player}. It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Paper covers rock. You lose!")
        else:
            print("Rock smashes scissors. You win!")
    elif player == "paper":
        if computer == "rock":
            print("Paper covers rock. You win!")
        else:
            print("Scissors cut paper. You lose!")
    elif player == "scissors":
        if computer == "rock":
            print("Rock smashes scissors. You lose!")
        else: 
            print("Scissors cut paper. You win!")
    else:
        ("Invalid selection. Please choose rock, paper or scissors.")

    repeat = input("Would you like to play again? Y/N \n").upper()
    if repeat != 'Y':
        break

