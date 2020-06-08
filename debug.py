import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)

print('What is ' + str(number1) + ' + ' + str(number2) + "?")
answer = input()
if answer == str(number1 + number2):
#Answer is a string, so the number 1 + 2 need to be converted using str() to compare value.
    print('Correct!')
else:
    print('Nope! The answer is ' + str(number1 + number2))
