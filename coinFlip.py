import random
import time

headsCount = 0
flips = 0

print("Out of 1000 flips, how many of them do you think will be heads?")

while flips < 1000:
    if random.randint(0, 1) == 1:
        headsCount += 1
    flips += 1
        

for i in range(3):
    print(".", end="")
    time.sleep(0.4)

print("There were " + str(headsCount) + " out of 1000")