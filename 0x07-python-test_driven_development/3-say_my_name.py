#!/usr/bin/python3
"""This is the say_my_name module
It defines a function that prints a first name and
last name
"""


def say_my_name(first_name, last_name=""):
    """say_my_name function prints the first and last name
    of a person.

    Args:
        first_name (str): first name to be printed.
        last_name (str, optional): last name to be printed.
        Defaults to "".

    Raises:
        TypeError: when first name is not a string
        TypeError: when last name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
