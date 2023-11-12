#!/usr/bin/python3
"""import Rectangle class"""


from models.rectangle import Rectangle


"""square classe (inherite from Rectangle)"""


class Square(Rectangle):
    """square classe (inherite from Rectangle)"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of a Square"""
        return (f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")
