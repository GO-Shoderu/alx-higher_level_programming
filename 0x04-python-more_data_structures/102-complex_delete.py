#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_list = []

    for i, j in a_dictionary.items():
        if j == value:
            new_list.append(i)

    for i in new_list:
        del a_dictionary[i]

    return (a_dictionary)
