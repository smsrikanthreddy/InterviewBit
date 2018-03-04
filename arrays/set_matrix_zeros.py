

def set_matrix_zero(A):
    m = len(A)
    n = len(A[0])
    rows = [0] * m
    cols = [0] * n
    for r_i in range(m):
        for c_j in range(n):
            if A[r_i][c_j] == 0:
                rows[r_i] = 1
                cols[c_j] = 1
    for r_i in range(m):
        for c_j in range(n):
            if rows[r_i] == 1 or cols[c_j] == 1:
                A[r_i][c_j] = 0
    return A


#import numpy as np
#A = np.matrix([[1,0,1,0],[1,1,1,0],[1,1,1,1]])
#B = np.matrix([[1,0,1],[1,1,1],[1,1,1]])
A = [[1,0,1],[1,1,1],[1,1,1]]

print('matrix zero is :-', set_matrix_zero(A))
