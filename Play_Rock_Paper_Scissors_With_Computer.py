import random

user_name = input("Welcome to Rock...Paper...Scissors...\n Please put your user name: ")
matches = input("Hi "+user_name+". How many times do you want to play RPS game: ")
matches = int(matches)

comp_score = 0
player_score = 0

for x in range(matches):

    print("Computer Score: "+str(comp_score)+"\n"+str(user_name)+" Score: "+str(player_score))
    # use randint to make the computer make a choice
    ran_num = random.randint(0, 2)

    # Human Choice
    human = input("Please Enter your choice against the computer! ::").lower()

    # Quiting Game before the end
    if human == "exit":
        break

    # Validate Human Input
    elif human not in ("rock", "paper", "scissors"):
        print("Please input either 'rock' 'paper' or 'scissors' ")

    # Game Logic
    elif ran_num == 0:
        computer_option = "rock"
        if human == "rock":
            print("Its a tie")
        elif human == "scissors":
            print("Computer Wins")
            comp_score += 1
        elif human == "paper":
            print("Human Wins!!")
            player_score += 1

    elif ran_num == 1:
        computer_option = "paper"
        print("Computer choice is: " + computer_option)
        if human == "rock":
            print("Computer Wins")
            comp_score += 1
        elif human == "scissors":
            print("Human Wins")
            player_score += 1
        elif human == "paper":
            print("Its a Tie!!")

    else:
        computer_option = "scissors"
        print("Computer choice is: " + computer_option)
        if human == "rock":
            print("Human Wins")
            player_score += 1
        elif human == "scissors":
            print("Its a Tie!!")
        elif human == "paper":
            print("Computer Wins!!")
            comp_score += 1

# End of Game
if comp_score > player_score:
    print("Sorry "+user_name+" try again next time.")
    print("Computer Score: "+str(comp_score) +"\n"+user_name+" Score: "+str(player_score))

if comp_score < player_score:
    print("Congratulations "+user_name+" you defeated the computer.")
    print("Computer Score: "+str(comp_score) +"\n"+user_name+" Score: "+str(player_score))


if comp_score == player_score:
    print("The match was a tie!!!")
    print("Computer Score: "+str(comp_score) +"\n"+user_name+" Score: "+str(player_score))



