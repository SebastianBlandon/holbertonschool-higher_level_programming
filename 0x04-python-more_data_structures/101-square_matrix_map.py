#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = [list(map(lambda x: pow(x, 2), row)) for row in matrix]
    return (new_matrix)
