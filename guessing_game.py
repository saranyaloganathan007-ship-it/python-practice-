import random

secret = random.randint(1, 10)

for attempt in range(3):
    guess = int(input("Guess a number from 1 to 10: "))

    if guess == secret:
        print("Correct! ")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print("Better luck next time!")
    print("The number was:", secret)

