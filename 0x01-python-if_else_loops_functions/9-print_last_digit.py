#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        lastDigit = number % 10
    elif number < 0:
        lastDigit = (number % -10) * -1
    elif number == 0:
        lastDigit = 0
    print("{:d}".format(lastDigit), end="")
    return lastDigit
