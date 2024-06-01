#2.number guessing game
import random
def guessing_num():
    given_num=random.randrange(0,1000)
    while True:
        guessed_num=int(input("Guess a number: "))
        if guessed_num>given_num:
            print("Too high!")
        elif guessed_num<given_num:
            print("Too low!")    
        else:
            print("You win! Congrats!")  
            break  
guessing_num()