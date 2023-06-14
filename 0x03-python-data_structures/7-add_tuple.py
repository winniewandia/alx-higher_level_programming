#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    a = tuple_a[:2]
    b = tuple_b[:2]
    a += (0,) * (2 - len_a)
    b += (0,) * (2 - len_b)
    result = (a[0] + b[0], a[1] + b[1])
    return result
