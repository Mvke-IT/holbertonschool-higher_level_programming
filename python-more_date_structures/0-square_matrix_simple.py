#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for m in matrix:
        new_matrix.appened(lis(map(lambda x: pow(x, 2), m )))
        return new_matrix
