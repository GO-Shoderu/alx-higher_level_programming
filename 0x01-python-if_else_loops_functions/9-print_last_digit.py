#!/usr/bin/python3

def print_last_digit(number):
    if (abs(number) % 10):
        print("{}".format(abs(number) % 10), end='')
    else:
        print("{}".format(0), end='')
    return (abs(number) % 10)
