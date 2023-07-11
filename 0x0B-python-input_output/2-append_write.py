#!/usr/bin/python3
"""This module contains the append_write function
"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added

    Args:
        filename (str, optional): name of file. Defaults to "".
        text (str, optional): text to be appended. Defaults to "".

    Returns:
        number of bytes: bytes appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
