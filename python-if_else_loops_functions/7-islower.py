#!/usr/bin/python3
def islower(c):
    """Check if a character is lowercase"""
    code = ord(c)
    if code >= 97 and code <= 122:
        return True
    return False
