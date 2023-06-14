#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keys = list(a_dictionary.keys())
    if key not in keys:
        return a_dictionary
    else:
        del a_dictionary['key']
        return a_dictionary
