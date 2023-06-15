#!/usr/bin/python3
def uniq_add(my_list=[]):
    j = 0
    for x in set(my_list):
        j += x
    return j
