import random

number = random.randint(10,50)
print("enter a number from 10 - 50 , let's check how lucky you are! /n")
print("you will win after you chatch the right word /n let's check your luck")

while True:
    guess = int(input("do your best ! @guest :"))
    if number == guess:
        print("u win the game")
        print("the number was",number)
        break
    else:
        print("try again !!!")
