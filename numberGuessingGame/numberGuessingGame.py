import random
import time
import os
import sys
import math

# Clears the users terminal for better readability
def clearAndSleep():
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(0.2)

clearAndSleep()

# Welcome message
print("""

Hello!
Welcome to this extravagant number guessing game!
You will be asked to enter two numbers, a lowest number and a highest number.
You will have to guess a random number between the two numbers.
Your total number of chances to guess the correct number will depend on how big the range of numbers are.""")

# Quits the game if the user does not want to play, forces the user to enter a valid choice of Yes or No
while True:
    try:
        willPlay = str.capitalize(input("\nWould you like to play? (Yes/No) "))
        clearAndSleep()

        if willPlay == "Yes":
            print("\nGreat! Let's get started!")   
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            break

        elif willPlay == "No":
            print("\nThat's too bad, hope to see you again soon!")
            time.sleep(2)
            sys.exit()

        else:
            clearAndSleep()
            print("\nInvalid input.")
        
    except ValueError:
        clearAndSleep()
        print("\nInvalid input. Please enter 'Yes' or 'No'")

# Gets user input for the lower and upper bounderies of the number range, also controls that the inputs are valid
while True:
    try:
        lowerBound = int(input("\nEnter the lowest number(must be 0 or higher): "))
        clearAndSleep()

        if lowerBound >= 0:
            break

        print("\nInvalid input. Number must be 0 or higher.")

    except ValueError:
        clearAndSleep()
        print("\nInvalid input. Please enter a whole number.")
        
while True:
    try:
        upperBound = int(input("\nEnter the highest number, it must be at least 3 higher than the lowest number(" + str(lowerBound) + "): "))
        clearAndSleep()

        if upperBound > lowerBound + 2:
            break

        print("\nInvalid input.")

    except ValueError:
        clearAndSleep()
        print("\nInvalid input. Please enter a whole number.")

# Generates random number using the user input, then calculates the total chances the user has to guess
numberToGuess = random.randint(lowerBound, upperBound)
totalChances = math.ceil(math.log(upperBound - lowerBound + 1) / math.log(2)) -1
guessCounter = 0

print("You will have " + str(totalChances) + " chances to guess to correct number from " + str(lowerBound) + " to " + str(upperBound) + ".\nGood luck!\n")

# Loop for guessing the number
while True:
    try:
        guessCounter += 1
        myGuess = int(input("Please enter your guess: "))

        if myGuess > upperBound or myGuess < lowerBound:
            print("Invalid guess! Please enter a number from " + str(lowerBound) + " to " + str(upperBound) + ".")
            guessCounter += -1

        elif myGuess == numberToGuess:
            clearAndSleep()
            print("\nWell done! You guessed the correct number! The number was " + str(numberToGuess) + " and you found it in " + str(guessCounter) + " attempts!") 
            break

        elif guessCounter == totalChances:
            print("\nWoopsie, you're out of guesses. The number was " + str(numberToGuess) + ", better luck next time!")
            break

        elif myGuess > numberToGuess:
            print("The number you guessed is too high.")

        elif myGuess < numberToGuess:
            print("The number you guessed is too low.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")
        guessCounter += -1

print("Press enter to quit...")
input()