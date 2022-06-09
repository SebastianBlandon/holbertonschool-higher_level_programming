#!/usr/bin/python3
"""
    Function pascal_triangle(n)
"""


def fact(num):
    if num < 0:
        return

    elif num == 0:
        return 1

    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact


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
