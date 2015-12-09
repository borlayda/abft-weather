#!/usr/bin/env python

from copy import copy, deepcopy

def iterate_matrix(matrix, r_checksum, c_checksum):
    '''
    Check if values are correct in a matrix
    defined by checksums.
    @param matrix : Fault tolerant matrix
    @type matrix : 2 dimensional array
    @param r_checksum : Computation summerize
        data about matrix values (rows)
    @type r_checksum : vector
    @param c_checksum : Computation summerize
        data about matrix values (columns)
    @type c_checksum : vector
    '''
    wrong_row = -1
    wrong_column = -1
    for vector in matrix:
        if not (check_checksum(vector, r_checksum[matrix.index(vector)])):
            wrong_row = matrix.index(vector)
    for vector in zip(*matrix):
        if not (check_checksum(vector, c_checksum[zip(*matrix).index(vector)])):
            wrong_column = zip(*matrix).index(vector)
    if (wrong_row > 0 and wrong_column > 0):
        matrix[wrong_row][wrong_column] = abs(r_checksum[wrong_row]-c_checksum[wrong_column])
    return matrix

def check_checksum(vector, checksum):
    '''
    Checks if there is any problem with the matrix
    and if it found any then it can correct one.
    @param vector : A line of a matrix (row or column)
    @type vector : array
    @param checksum : Counted value of the sum of
        all values in vector
    @type checksum : float
    '''
    counted_sum = 0.0
    for value in vector:
        counted_sum += float(value)
    return counted_sum == checksum

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
    summ_matrix = deepcopy(matrix_array[0])
    row_checksum = [0 for vector in summ_matrix]
    column_checksum = [0 for vector in zip(*summ_matrix)]
    for matrix in matrix_array[1:]:
        summ_matrix = add_matrices(summ_matrix, matrix)
        for vector in summ_matrix:
            row_checksum[summ_matrix.index(vector)] = count_checksum(vector)
        for vector in zip(*summ_matrix):
            column_checksum[zip(*summ_matrix).index(vector)] = count_checksum(vector)
    return summ_matrix, column_checksum, row_checksum
    
def print_matrix(matrix):
    '''
    Better format to write out matrix
    @param matrix : matrix source
    @type matrix : 2 dimensional array
    '''
    content = ""
    head = "    \t"
    for i in range (0, len(matrix[0])):
        head += " {0}  \t".format(i+1)
    head += "\n   "
    head += "    \t"
    for i in range (0, len(matrix[0])):
        head += "--- \t"
    head += "\n"
    body = ""
    for vector in matrix:
        body += " {0} |\t".format(matrix.index(vector)+1)
        for value in vector:
            body += " {0} |\t".format(value)
        body += "\n"
    content = head + body
    print content
    
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
    matrix, csum, rsum = make_summ(matrices)
    print_matrix(matrix)
    iterate_matrix(matrix, rsum, csum)
    print "\n"
    print_matrix(matrix)
