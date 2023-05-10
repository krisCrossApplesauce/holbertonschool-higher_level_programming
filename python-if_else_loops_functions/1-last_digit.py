#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
if number < 0:
    last = last * -1
print(f"Last digit of {number} is {last} and is", end=' ')
if last == 0:
    print(f"0")
elif last < 6:
    print(f"less than 6 and not 0")
else:
    print(f"is greater than 5")
