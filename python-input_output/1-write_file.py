#!/usr/bin/python3

"""
This function for writing to file
"""


def write_file(filename="", text=""):
    """
    This function is for writing to file
    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
