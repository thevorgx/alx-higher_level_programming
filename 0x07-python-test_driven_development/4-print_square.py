#!/usr/bin/python3
"""print square"""


def print_square(size=10):
    """print square"""

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            if j != (size - 1):
                print('#', end='')
            else:
                print("#")
