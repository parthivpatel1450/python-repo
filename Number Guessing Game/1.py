"""
Number Guessing Game :
 Build a simple number guessing game to test your luck.
Requirements:

It is a CLI-based game, so you need to use the command line to interact with the game. The game should work as follows:

When the game starts, it should display a welcome message along with the rules of the game.

The computer should randomly select a number between 1 and 100.

User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.

The user should be able to enter their guess.

If the user's guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.

If the user's guess is incorrect, the game should display a message indicating whether the number is greater or less than the user's guess.

The game should end when the user guesses the correct number or runs out of chances.
"""



import random
print("_ _ _ _ _ _ _ _ _ _ Welcome to Number Guessing Game_ _ _ _ _ _ _ _ _ _ ")
print("Game Rules")
print("1.you have to choose a number that is between 1 to 100.")
print("2.when your number is same as computer have choosen then you will win the Game.")
print("3.you have to select a difficulty level and according to it you will get total numbers of attempts.")
print("4.when your numbers of attempts complete you lose the Game.")

a=random.randint(1,100)

n=input("Enter your difficulty level (easy,medium,hard) : ").lower()

if n=="easy":
    print("you have 10 attemts to guess a number")
    chances=10

elif n=="medium":
    print("you have 7 attemts to guess a number")
    chances=7

elif n=="hard":
    print("you have 5 attemts to guess a number")
    chances=5

else:
    print("Invalid Input!")
    exit()

attempts=0
while 0<chances:
    try:
        user_guess = int(input("Enter your number : "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if user_guess < 1 or user_guess > 100:
        print("Enter number between 1 and 100!")
        continue

    attempts+=1

    if a==user_guess:
        print("congratulations, you have chosen a correct number")
        print(f"You guessed it in {attempts} attempts!")
        print("You won The Game")
        break
    elif a>user_guess:
        print("The number is greater than your guess.")
    else:
        print("number is smaller than guess number")
    chances-=1
    print(f"you have left {chances} chances")

else:
    print("runs out of chances")
    print(f"The correct number was: {a}")
    print("you lose the Game")







