#!/usr/bin/python3
""" Module matrix divided
    Prototype: def matrix_divided(matrix, div):

"""


def matrix_divided(matrix, div):
    """ Funcion matrix_divided
        Args:
            matrix (list of lists of int or float): input matrix
            div (int or float): input value
        Return:
            new matrix or raise error
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")

    if not len(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    rows = [row for row in matrix if type(row) is list]
    new_matrix = []
    len_rows = []
    if all(rows):
        for row in range(len(matrix)):
            if type(matrix[row]) is not list:
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")
            if not row:
                len_rows.append(len(matrix[row]))
            else:
                len_rows.append(len(matrix[row]))
                if len_rows[row] is not len_rows[row - 1]:
                    raise TypeError("Each row of the matrix must have"
                                    " the same size")
            new_row = []
            for i in range(len(matrix[row])):
                if type(matrix[row][i]) is not int:
                    if type(matrix[row][i]) is not float:
                        raise TypeError("matrix must be a matrix"
                                        " (list of lists) of integers/floats")
                new_row.append(round(matrix[row][i] / float(div), 2))
            new_matrix.append(new_row)
        return new_matrix
