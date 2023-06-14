#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new = []
    for i in matrix:
        new = i
        for j in new:
            print("{:d}".format(j), end=' ')
        print()
