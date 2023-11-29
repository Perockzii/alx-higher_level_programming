#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Lastdigit = abs(number) % 10
if number < 0:
    Lastdigit = -(Lastdigit)
thestring = "Last digit of {} is {}".format(number, Lastdigit)
if Lastdigit > 5:
    print(f"{thestring} and is greater than 5")
elif Lastdigit == 0:
    print(f"{thestring} and is 0")
elif Lastdigit < 6 != 0:
    print(f"{thestring} and is less than 6 and not 0")

