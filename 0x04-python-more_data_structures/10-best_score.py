#!/usr/bin/python3

def best_score(a_dictionary):
    high = a_dictionary[next(iter(a_dictionary))]
    key = ''

    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)

    for elem in a_dictionary:
        if a_dictionary[elem] > high:
            high = a_dictionary[elem]
            key = elem

    return (key)
