import random
while True:
    user_action = input("enter a choice (ROCK 🪨 , PAPER 📜 , scissor ✂️ ) :")
    possible_action = ["rock","paper","scissor"]
    computer_action = random.choice (possible_action)

    if user_action == computer_action:
        print(f"both have chosen the same , it's a tie !")
    elif user_action == "rock":
        if computer_action == "scissor":
            print("you win !")
        else :
            print("computer wins !")
    elif user_action == "paper":
            if computer_action == "scissor":
                print("computer wins !")
            else :
                print("you win !")
    elif user_action == "scissor":
            if computer_action == "paper":
                print("you win !")
            else :
                print("computer wins !")

    play = input("play again ! (y/n)")
    if play != "y":
        break

