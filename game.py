#game.py
#rock, paper, scissors game

import os
import random

from dotenv import load_dotenv
#https://github.com/theskumar/python-dotenv

load_dotenv()

USER_NAME = os.getenv("USER_NAME", default="Player One")


terminology = True


#fetch new username from .env?




def rpsgame():
    terminology = True

    print("-------------------")
    print("Welcome",USER_NAME,"to my Rock-Paper-Scissors game...")
    print("-------------------")

    while terminology:
        userplay = input("Please choose either 'rock', 'paper', or 'scissors':")
        if userplay=='rock' or userplay=='paper' or userplay== 'scissors':
            terminology=False
        elif userplay!='rock' or userplay!='paper' or userplay!= 'scissors':
            print()
            print("Please enter either 'rock', 'paper', or 'scissors'.")
            print()

    print("Rock, Paper, Scissors, Shoot!")
    print("You chose:", userplay)

    computerChoice =random.choice(['rock','paper','scissors'])
    print("The computer chose:",computerChoice)
    if computerChoice==userplay:
        result = "It's a tie!"
    elif computerChoice=='rock':
        if userplay=='scissors':
            result = "Oh, the computer won. It's ok. Try again!"
        if userplay=='paper':
            result= "Congratulations, you beat the computer and won! :)"
    elif computerChoice=='paper':
        if userplay=='scissors':
            result= "Congratulations, you beat the computer and won! :)"
        if userplay=='rock':
            result = "Oh, the computer won. It's ok. Try again!"
    elif computerChoice=='scissors':
        if userplay=='rock':
            result= "Congratulations, you beat the computer and won! :)"
        if userplay=='paper':
            result = "Oh, the computer won. It's ok. Try again!"


    print("-------------------")
    print(result)
    print("-------------------")
    print("Thanks for playing. Please play again!")



#print("Rock, Paper, Scissors, Shoot!")

rpsgame()
