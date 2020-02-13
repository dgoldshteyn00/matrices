"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math


# print the matrix such that it looks like
# the template in the top comment
def print_matrix(matrix):
    cols = len(matrix)
    rows = len(matrix[0])
    for i in range(0, rows):
        for j in range(0, cols):
            print(str(matrix[j][i]) + " ")
            if j == cols - 1:
                print("\n")


# turn the parameter matrix into an identity matrix
# you may assume matrix is square
def identity(matrix):
    n = len(matrix)
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = 0
    for i in range(0, n):
        matrix[i][i] = 1
    print_matrix(matrix)


# multiply m1 by m2, modifying m2 to be the product
# m1 * m2 -> m2
def matrix_multiply(m1, m2):
    result = new_matrix()
    for i in range(0, len(m1)):
        for j in range(0, len(m2[0])):
            for k in range(0, len(m2)):
                result[i][j] += m1[i][k] * m2[j][k]
    m2 = result
    print_matrix(m2)


def new_matrix(rows=4, cols=4):
    m = []
    for c in range(cols):
        m.append([])
        for r in range(rows):
            m[c].append(0)
    return m


matrix1 = new_matrix()
matrix2 = new_matrix()

identity(matrix1)

matrix_multiply(matrix1, matrix2)
