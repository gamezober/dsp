# Matrix Algebra

import numpy as np

#Create Matrices

#A
A = np.matrix([[1, 2, 3], [2, 7, 4]])

#B
B = np.matrix([[1 , -1], [0, 1]])

#C
C = np.matrix([[5, -1], [9, 1], [6, 0]])

#D
D = np.matrix([[3, -2, -1], [1, 2, 3]])

#u
u = np.matrix([6, 2, -3, 5])

#v
v_list  = [3, 5, -1, 4]
v = np.matrix(v_list)

#w
w_list = [1, 8, 0, 5]
w = np.matrix(w_list)
w = np.matrix(w_list).transpose()

#Matrix Dimensions
matrices = {'A': A, 'B': B,'C': C, 'D': D, 'u': u, 'w': w}
dim_dict = {i : matrices[i].shape for i in matrices}

for i in dim_dict:
    print i, matrices[i].shape
#Ans:
#A (2, 3)
#C (3, 2)
#B (2, 2)
#D (2, 3)
#u (1, 4)
#w (4, 1)

#Vector Operations
#2.1
u + v
# Ans: matrix([[ 9,  7, -4,  9]])

#2.2
u - v
#Ans: matrix([[ 3, -3, -2,  1]])

#2.3
6 * u
#Ans: matrix([[ 36,  12, -18,  30]])

#2.4
#Transpose T for dot product with v
v_t = v.T
u * v_t
#Ans: matrix([[51]])

#2.5

np.linalg.norm(u)
#Ans: = 8.6

#Matrix Operations

#3.1
A + class
#Ans: Not Defined - Shapes not Alligned

#3.2
A - C.T
# Ans:
#matrix([[-4, -7, -3],
#        [ 3,  6,  4]])

#3.3
C.T + (3 * D)
#Ans:
#matrix([[14,  3,  3],
#        [ 2,  7,  9]])

#3.4
B * A
# Ans:
#matrix([[-1, -5, -1],
#        [ 2,  7,  4]])

#3.5
B * A.T
#Ans:
#Not Defined - Shapes not alligned

#Optional

#3.6
B * C
#Not Defined - Shapes not alligned

#3.7
C * B
#Ans:
#matrix([[ 5, -6],
#        [ 9, -8],
#        [ 6, -6]])
