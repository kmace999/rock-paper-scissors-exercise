#game.py
#rock, paper, scissors game

import time
import random

username = 'Player One'


#fetch new username from .env?

def rpsgame():
    delay = 3
    print("-------------------")
    print("Welcome",username,"to my Rock-Paper-Scissors game...")
    print("-------------------")
    computerChoice =random.choice(['rock','paper','scissors'])

    terminology = True

    while terminology:
        userplay = input("Please choose either 'rock', 'paper', or 'scissors':")
        if userplay=='rock' or userplay=='paper' or userplay== 'scissors':
            terminology=False


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



    print("Rock, Paper, Scissors, Shoot!")
    print("You chose:", userplay)
    time.sleep(delay)
    print("The computer chose: ",computerChoice)
    print("-------------------")
    print(result)
    print("-------------------")
    print("Thanks for playing. Please play again!")



#print("Rock, Paper, Scissors, Shoot!")

rpsgame()
