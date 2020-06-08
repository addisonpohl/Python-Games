# guess the number
import random

number = random.randint(1, 20)

print("Hello, what's your name?")
myName = input()
print("Well " + myName + ", I'm thinking of a number between 1 and 20?")

for i in range(3):
    print("Take a guess...")
    guess = int(input())
    if guess > number:
        print("Lower")

    if guess < number:
        print("higher")

    if guess == number:
        break

if guess != number:
    number = str(number)
    print("Nope, the number I was thing of was " + number)

if guess == number:
    print("You got it!")
