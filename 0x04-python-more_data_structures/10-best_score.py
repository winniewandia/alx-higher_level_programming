#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    keys = a_dictionary.keys()
    max = 0
    for k in keys:
        if a_dictionary[k] > max:
            max = a_dictionary[k]
    return k
