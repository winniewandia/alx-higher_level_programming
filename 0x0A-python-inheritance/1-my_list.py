#!/usr/bin/python3
"""This module is called my_list and 
contains a class
"""


class MyList(list):
    """a class MyList that inherits from list

    Args:
        list (list): list to be printed in ascending order
    """

    def print_sorted(self):
        sorted_l = self.copy()
        sorted_l.sort()
        print(sorted_l)
