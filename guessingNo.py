#Level 2
#Task 1:Guessing Game

import random

def guess_number():

    no = random.randint(1, 100)
    guess = -1
    while guess != no:
        guess = int(input("Guess a no b/w 1 & 100: "))
        if guess < no:
            print("Too low.")
        elif guess > no:
            print("Too high.")
    return guess


def main():
    print(" GUESSING NUMBER GAME.")

    guess = guess_number()
    print("Congratulations! You guessed the no {} correctly.".format(guess))

if __name__ == "__main__":
    main()
                
