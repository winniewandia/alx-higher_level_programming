#!/usr/bin/python3
"""This module contains a read_file function
"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): name of file to be read Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
