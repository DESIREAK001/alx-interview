#!/usr/bin/python3
"""
0-validate_utf8.py
"""


def binary(number):
    '''
        checks and returns the number of leading ones
        if the number is not valid it returns -1
    '''
    for a in range(7, 2, -1):
        if not number >> a & 1:
            return 7 - a
    return -1


def validUTF8(data):
    '''
        determines if a given data set represents a valid UTF-8 encoding
    '''
    prev = 0
    for number in data:
        n_bytes = binary(number)
        if prev == 0:
            if n_bytes == 1:
                return False
            else:
                prev = n_bytes
        elif n_bytes != 1:
            return False
        prev = prev - 1 if prev != 0 else prev

    return prev == 0
