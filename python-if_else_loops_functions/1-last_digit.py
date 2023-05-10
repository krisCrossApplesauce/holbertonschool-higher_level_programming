#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
else:
    last = number % 10
print(f"Last digit of {number} is {last} and is", end=' ')
if last == 0:
    print(f"0")
elif last < 6:
    print(f"less than 6 and not 0")
else:
    print(f"greater than 5")
