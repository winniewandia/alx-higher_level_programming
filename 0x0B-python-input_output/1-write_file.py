#!/usr/bin/python3
"""This module contains the write_file function
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename (str, optional): file to be opened. Defaults to "".
        text (str, optional): text to be written. Defaults to "".

    Returns:
        number of bytes: bytes written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
