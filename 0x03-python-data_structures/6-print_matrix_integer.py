#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        print(*('{:d}'.format(i) for i in n))
