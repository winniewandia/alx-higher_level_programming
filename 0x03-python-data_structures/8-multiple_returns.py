#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not length:
        return None
    else:
        tuple = (length, sentence[0])
    return tuple
