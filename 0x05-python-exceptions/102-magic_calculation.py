#!/usr/bin/python3
def magic_calculation(a, b):
    rzllt = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                rzllt += (a ** b) / i
        except Exception:
            rzllt = b + a
            break
    return (rzllt)
