#!/usr/bin/env python

from copy import copy

def iterate_matrix(matrix, checksum):
    '''
    Check if values are correct in a matrix
    defined by checksums.
    @param matrix : Fault tolerant matrix
    @type matrix : 2 dimensional array
    @param checksum : Computation summerize
        data about matrix values
    @type checksum : vector
    '''
    for vector in matrix:
        check_checksum(vector, checksum)
    return matrix

def count_checksum(vector):
    '''
    Vector value addition for checksum
    of the column or row.
    @param vector : matrix column or row
    @type vector : array
    '''
    checksum = 0.0
    for value in vector:
        checksum += float(value)
    return checksum

def get_matrix():
    data = get("rasberrypy.com")
    try:
        matrices = data.json()["matrices"]
        checksums = data.json()["checksums"]
    except:
        matrices = data.json()

def add_matrices(matrix1, matrix2):
    '''
    Adds two matrices to each other value
    by value.
    @param matrix1 : First matrix
    @type matrix1 : 2 dimensional array
    @param matrix2 : Second matrix
    @type matrix2 : 2 dimensional array 
    '''
    if (len(matrix1) != len(matrix2)):
        raise Exception("Invalid operation:\n"+
                        "Addition of two not equal dimensional matrices!")
    result = copy(matrix1) 
    for index2 in range(0, len(matrix2)):
        if (len(result[index2]) != len(matrix2[index2])):
            raise Exception("Invalid operation:\n"+
                        "Addition of two not equal dimensional matrices!")
        for inner_index in range(0, len(matrix2[index2])):
            result[index2][inner_index] += matrix2[index2][inner_index] 
    return result

def make_summ(matrix_array):
    '''
    Summerize the values in matrices.
    Also makes a checksum, to verify the
    result of computation.
    @param matrix_array : Impot data a bunch of
        matrices with numeric values
    @type matrix_array : array of 2 dimensional
        arrays 
    '''
    summ_matrix = matrix_array[0]
    row_checksum = [0 for vector in summ_matrix]
    column_checksum = [0 for vector in zip(*summ_matrix)]
    for matrix in matrix_array[1:]:
        summ_matrix = add_matrices(summ_matrix, matrix)
        for vector in summ_matrix:
            row_checksum[summ_matrix.index(vector)] = count_checksum(vector)
        for vector in zip(*summ_matrix):
            column_checksum[zip(*summ_matrix).index(vector)] = count_checksum(vector)
        print summ_matrix, row_checksum, column_checksum
        
if __name__ == "__main__":
    '''
    Example application for running
    '''
    matrices = [
     [[1, 2], [3, 4], [5, 6]],
     [[7, 8], [9, 1], [2, 3]],
     [[4, 5], [6, 7], [8, 9]],
     [[1, 2], [3, 4], [5, 6]],
     [[7, 8], [9, 1], [2, 3]],
     [[4, 5], [6, 7], [8, 9]],
     [[1, 2], [3, 4], [5, 6]]
    ]
    make_summ(matrices)
