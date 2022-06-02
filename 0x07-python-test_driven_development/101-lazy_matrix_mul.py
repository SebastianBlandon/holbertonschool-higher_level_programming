#!/usr/bin/python3
""" function that multiplies 2 matrices by using the module NumPy """
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Funtion that multiples two matrices
        Args:
            m_a (list of lists (ints or floats)): matrix a
            m_b (list of lists (ints or floats)): matrix b
        Return:
            the result operation with matrix

    """
    return (numpy.matmul(m_a, m_b))
