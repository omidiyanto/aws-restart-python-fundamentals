import random

# print instructions
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#store number to guessed in variables
number = random.randint(1,10)

# while loop to always ask to user to guess the right number
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))