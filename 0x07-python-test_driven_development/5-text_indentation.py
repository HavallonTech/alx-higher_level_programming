#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    text_indentation: the functon prints a text followed by a blank line.

    Attributes:
        text: The text to be printed

    Example:
    >>> text_indentation("wisdom Honest")
    Wisdom
    <BLANKLINE>
    Honest
    """
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")

    arrayOfText = text.split()
    charac = {"?", ".", ":"}

    for _words in arrayOfText:
        print(_words, end="")

        if not (set(_words) & charac):
            if not (_words == arrayOfText[-1]):
                print(" ", end="")
                

        if set(_words) & charac:
            print("\n")
