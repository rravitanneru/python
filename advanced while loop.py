# while loop is useful when we dont know iterations are required

# coding for guessing game

import  random
n =20 # ranging from 0 to 20
to_be_guessed = int (n*random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("number:"))
    if guess > 0:
     if guess > to_be_guessed:
        print ("number to large")
     elif guess < to_be_guessed:
        print("numbrt too small")
    else:
        print("you lost the game")
        break
else:
    print("congrtas you won the game")