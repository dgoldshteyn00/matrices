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
    x = y = z = ""
    ones = ""
    for i in range(len(matrix)):
        x += str(matrix[i][0]) + " "
        y += str(matrix[i][1]) + " "
        z += str(matrix[i][2]) + " "
        ones += str(matrix[i][3]) + " "
    print(x + "\n")
    print(y + "\n")
    print(z + "\n")
    print(ones + "\n")


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
    result = new_matrix(cols=len(m2))
    for i in range(0, len(m2)):
        for j in range(0, len(m1[0])):
            for k in range(0, len(m1)):
                result[i][j] += m1[i][k] * m2[k][j]
    for i in range(len(result)):
        for j in range(len(result[0])):
            m2[i][j] = result[i][j]
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
