import random

# use randint to make the computer make a choice
ran_num = random.randint(0, 2)

# Human Choice
human = input("Please Enter your choice against the computer! ::").lower()

# Validate Human Input
if human not in ("rock", "paper", "scissors"):
    print("Please input either 'rock' 'paper' or 'scissors' ")
    # human = input("Please Enter your choice against the computer! ::").lower()


# Game Logic
elif ran_num == 0:
    computer_option = "rock"
    # human = input("Please Enter your choice against the computer! ::").lower()
    print("Computer choice is: " + computer_option)
    if human == "rock":
        print("Its a tie")
    elif human == "scissors":
        print("Computer Wins")
    elif human == "paper":
        print("Human Wins!!")



elif ran_num == 1:
    computer_option = "paper"

    # human=input("Please Enter your choice against the computer! ::").lower()
    print("Computer choice is: " + computer_option)
    if human == "rock":
        print("Computer Wins")
    elif human == "scissors":
        print("Human Wins")
    elif human == "paper":
        print("Its a Tie!!")


else:
    computer_option = "scissors"
    # human = input("Please Enter your choice against the computer! ::").lower()
    print("Computer choice is: " + computer_option)
    if human == "rock":
        print("Human Wins")
    elif human == "scissors":
        print("Its a Tie!!")
    elif human == "paper":
        print("Computer Wins!!")
