import time
import random

def displayIntro():
    print('''
    You are in a land full of dragons.
    In front of you, you see two caves. 
    In one cave, the dragon is friendly and will share his treasure with you. 
    The other dragon is greedy and will eat you on sight.''' )
    print()

def chooseCave():
    cave = " "
    while cave != "1" and cave != "2":
        print("Will you choose cave 1 or 2?")
        cave = input()
    return cave

def checkCave(caveChosen):
    tresure = random.randint(1, 2)
    print("You approach the cave...")
    time.sleep(1)
    print("A large dragon approaches you! He opens his jaws and...")
    time.sleep(2)

    if caveChosen == str(tresure):
        print("\nGrants you his treasure!\n")
    else:
        print("\nEnds you where you stand...\n")

keepPlaying = "yes"
while keepPlaying == "yes" or keepPlaying == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print("Would you like to play again? ('yes' or 'no')")
    keepPlaying = input().lower()

