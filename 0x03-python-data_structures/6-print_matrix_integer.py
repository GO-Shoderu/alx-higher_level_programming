#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or matrix is None:
        print("{}".format('\n'))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end=' ')
