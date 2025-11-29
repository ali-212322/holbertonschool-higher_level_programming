#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        ascii_code = ord(ch)
        if ascii_code >= 97 and ascii_code <= 122:
            ch = chr(ascii_code - 32)
        print("{}".format(ch), end="")
    print()
