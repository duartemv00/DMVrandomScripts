import random

choices = ["rock","paper","scissors"]

while True:
    computer = random.choice(choices)
    player = None
    while player not in choices:
        try:
            player = input("rock, paper or scissors?: ").lower()
        except:
            print("Not a valid choice")
    print("Computer: "+computer)
    print("player: "+player)
    if player==computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Player loses")
        if computer == "scissors":
            print("Player wins")
    elif player == "paper":
        if computer == "scissors":
            print("Player loses")
        if computer == "rock":
            print("Player wins")
    elif player == "scissors":
        if computer == "rock":
            print("Player loses")
        if computer == "paper":
            print("Player wins")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Thanks for playing!")