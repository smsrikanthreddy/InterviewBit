

def setZeroes(A):
    m = len(A)
    n = len(A[0])
    rows = [1] * m
    cols = [1] * n
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                rows[i] = 0
                cols[j] = 0
    #print(rows, cols)
    for i in range(m):
        for j in range(n):
            if rows[i]==0 or cols[j] == 0:
                A[i][j] = 0
    return A


#import numpy as np
A = [[1,0,1],[1,1,1],[1,1,1]]
import pdb
pdb.set_trace()
print('matrix zero is :-', setZeroes(A))
