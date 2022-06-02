#!/usr/bin/python3
""" Module that contains a function for multiplie 2 matrices"""


def matrix_mul(m_a, m_b):
    """ Funtion that multiples two matrices
        Args:
            m_a (list of lists (int or floats)): matrix a
            m_b (list of lists (int or floats)): matrix b
        Return:
            the result matrix
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all([isinstance(item, list) for item in m_a]):
        raise TypeError("m_a must be a list of lists")

    if not all([isinstance(item, list) for item in m_b]):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or not all(len(item) != 0 for item in m_a):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or not all(len(item) != 0 for item in m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_b should contain only integers or floats")

    if not all([len(item) == len(m_a[0]) for item in m_a]):
        raise TypeError("each row of m_a must be of the same size")

    if not all([len(item) == len(m_b[0]) for item in m_b]):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    n_mul = 0
    mul = []
    all_mul = []
    lim = max(len(m_a), len(m_b))
    for row_a in m_a:
        for i in range(lim):
            for j in range(len(m_b)):
                n_mul += row_a[j] * m_b[j][i]
            mul.append(n_mul)
            n_mul = 0
        all_mul.append(mul)
        mul = []
    return all_mul
