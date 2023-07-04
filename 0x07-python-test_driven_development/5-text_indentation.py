#!/usr/bin/python3
"""This module is called the 5-text_indentation.
It defines a function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """This function prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text (str): string to be split

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    copy = text[:]
    for d in ".?:":
        token = copy.split(d)
        copy = ""
        for j in token:
            j = j.strip(" ")
            copy = j + d if copy is "" else copy + "\n\n" + j + d
    print(copy[:-3], end="")
