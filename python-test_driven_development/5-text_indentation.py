#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after each . ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: . ? and :

    Args:
        text: text to be printed

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    last = " "
    for letter in text:
        if letter == " " and last == " ":
            continue
        if (last == "?" or last == "." or last == ":") and letter == " ":
            continue
        if letter == "?" or letter == "." or letter == ":":
            print("{}\n".format(letter))
        else:
            print(letter, end="")
        last = letter
