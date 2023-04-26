#!/usr/bin/python3
''' divides all elements of a matrix '''


def matrix_divided(matrix, div):
    ''' divides matrix by div, rounded to 2 decimal places '''
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in l] for l in matrix]
