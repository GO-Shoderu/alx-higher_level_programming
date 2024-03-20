#!/usr/bin/python3

def weight_average(my_list=[]):
    new_list = []
    count = 0

    if len(my_list) == 0:
        return (0)

    for i in my_list:
        new_list.append(i[0] * i[1])
        count += i[1]

    return (sum(new_list) / count)
