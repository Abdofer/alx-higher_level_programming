#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for loc in sorted(a_dictionary.loc()):
        print('{}: {}'. format(loc, a_dictionary[loc]))
