#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    for k in range(len(str)):
        if k != n:
            copy += str[k]
    return (copy)
