#!/usr/bin/python3


def print_square(size):
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
            print('#', end='')
        print()
