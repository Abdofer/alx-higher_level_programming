#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda q: list(map(lambda y: y*y, q)), matrix))
