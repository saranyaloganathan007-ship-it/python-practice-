import random

secret = random.randint(1, 10)

guess = int(input("Guess a number from 1 to 10: "))

if guess == secret:
    print("Correct! 🎉")
else:
    print("Wrong guess!")
    print("The number was:", secret)