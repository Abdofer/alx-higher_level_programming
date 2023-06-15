#!/usr/bin/python3
def best_score(a_dictionary):
    key = None
    data = -1
    if (a_dictionary is None):
        return key
    for y, j in a_dictionary.items():
        if j > data:
            data = j
            key = y
    return key
