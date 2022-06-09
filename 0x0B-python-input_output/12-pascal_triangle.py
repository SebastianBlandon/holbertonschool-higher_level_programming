#!/usr/bin/python3
"""
    Function pascal_triangle(n)
"""
from math import factorial as fact


def pascal_triangle(n):
    """ Function  that returns a list of lists of integers
    representing the Pascal’s triangle of n:

        Args:
            n (int): input integer
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        pascal = []
        for j in range(i+1):
            pascal.append(int(fact(i)/(fact(j)*fact(i-j))))
        triangle.append(pascal)
    return triangle
