#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self._condition = None

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New" 

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        if isinstance(value, str):
            self._condition = value
        else:
            print("Condition must be a string")

