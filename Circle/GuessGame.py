#This is a simple game to guess a random number. This porgram shows the circle structure and the basic use of i/o

import random

answer = random.randint(1, 100)
guessTime = 0

while True:
    guessNumber = int(input("Guess a number between 1 to 100: "))

    if guessNumber > 100 or guessNumber < 1:
        print("Please guess a number within 1 ~ 100.")
        continue
    elif guessNumber == answer:
        print("You are right!")
        break
    elif guessNumber > answer:
        print("A little bigger. Guess again (^_^)")
    else:
        print("A little smaller. Guess again (^_^)")

    guessTime += 1

print(" The answer is %d, you have guess %d times!" %(answer, guessTime))