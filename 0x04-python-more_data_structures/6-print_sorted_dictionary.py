#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_d = list(a_dictionary.keys())
    sorted_d.sort()
    for k in sorted_d:
        print("{}: {}".format(k, a_dictionary.get(k)))
