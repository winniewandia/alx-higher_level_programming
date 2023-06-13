#!/usr/bin/python3
for num in range(0, 10):
    for i in range(0, 10):
        if i != num and num < i:
            if num != 8 or i != 9:
                print("{}{}".format(num, i), end=', ')
            else:
                print("{}{}".format(num, i))
