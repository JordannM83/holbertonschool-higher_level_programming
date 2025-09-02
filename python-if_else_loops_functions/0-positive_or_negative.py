#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("%i is positive" % number)
elif number == 0:
    print("%i is zero" % number)
elif number < 0:
    print("%i is negative" % number)
