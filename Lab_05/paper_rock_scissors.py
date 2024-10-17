import random

mylist = ["Rock", "Paper", "Scissor"]

def gameplay():
    rounds = 3
    while True:
        computer = random.choice(mylist)
        player = input("Rock - Paper - Scissor?")
        if computer.upper() == player.upper():
            print("Computer Choose:", computer)
            print("Draw match!")
            print("You need {} to win".format(rounds))
        elif player.upper() == "ROCK":
            if computer.upper() == "PAPER":
                print("Computer Choose:", computer)
                print("You lose!")
                print("You need {} to win".format(rounds))
            if computer.upper() == "SCISSOR":
                rounds -= 1
                print("Computer Choose:", computer)
                print("You win!")
                print("You need {} to win".format(rounds))
        elif player.upper() == "PAPER":
            if computer.upper() == "SCISSOR":
                print("Computer Choose:", computer)
                print("You lose!")
                print("You need {} to win".format(rounds))
            if computer.upper() == "ROCK":
                rounds -= 1
                print("Computer Choose:", computer)
                print("You win!")
                print("You need {} to win".format(rounds))
        elif player.upper() == "SCISSOR":
            if computer.upper() == "ROCK":
                print("Computer Choose:", computer)
                print("You lose!")
                print("You need {} to win".format(rounds))
            if computer.upper() == "PAPER":
                rounds -= 1
                print("Computer Choose:", computer)
                print("You win!")
                print("You need {} to win".format(rounds))
        else:
            print("Invalid syntax!")

        if rounds == 0:
            break

gameplay()

    
