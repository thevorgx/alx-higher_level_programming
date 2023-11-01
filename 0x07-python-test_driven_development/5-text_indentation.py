#!/usr/bin/python3
"""prints a text"""


def text_indentation(text):
    """prints a text"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    special_chars = set(['.', '?', ':'])
    result = []
    paragraph = []

    for char in text:
        paragraph.append(char)

        if char in special_chars:
            result.append(''.join(paragraph))
            paragraph = []

    if paragraph:
        result.append(''.join(paragraph))

    for paragraph in result:
        print(paragraph.strip())
        print()
