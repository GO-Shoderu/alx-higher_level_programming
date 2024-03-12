#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97:
            if i+1 == len(str):
                print("{}".format(chr(ord(str[i]) - 32)))
            else:
                print("{}".format(chr(ord(str[i]) - 32)), end='')
        else:
            if i+1 == len(str):
                print("{}".format(str[i]))
            else:
                print("{}".format(str[i]), end='')
