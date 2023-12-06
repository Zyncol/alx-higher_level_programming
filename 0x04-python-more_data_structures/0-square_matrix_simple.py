#!/usr/bin/python3
# squares all integers
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda y: y * y, row)) for row in matrix])
