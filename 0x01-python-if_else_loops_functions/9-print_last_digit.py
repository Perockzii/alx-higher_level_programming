#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    last_digit = number % 10
    print("{}".format(last_digit), end='')
    return (last_digit)  
