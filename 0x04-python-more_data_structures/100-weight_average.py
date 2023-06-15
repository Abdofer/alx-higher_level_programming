#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    pes, haramo = 0, 0
    for n1, n2 in my_list:
        pes += n1 * n2
        haramo += n2
    return pes / haramo
