#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
result = number % 10 if number >= 0 else -number % 10
if number < 0:
    result = -result
if result > 5:
    print(f"Last digit of {number} is {result} and is greater than 5")
elif result == 0:
    print(f"Last digit of {number} is {result} and is 0")
elif result < 6 and result != 0:
    print(
        f"Last digit of {number} is {result} and is less than 6 and not 0")
