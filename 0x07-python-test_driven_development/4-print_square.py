#!/usr/bin/python3
"""print square"""


def print_square(size=10):
    """print square"""

    message = "size must be an integer"
    if isinstance(size, float) and size < 0:
        raise TypeError(message)
    if not isinstance(size, int):
        raise TypeError(message)
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            if j != (size - 1):
                print('#', end='')
        print()
