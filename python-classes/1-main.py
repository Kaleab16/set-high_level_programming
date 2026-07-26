#!/usr/bin/python3
square = __import__('1-square').square

my_square = square(3)
print(type(my_square))
print(my_square.__dict__)
