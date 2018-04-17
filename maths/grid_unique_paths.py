# @param A : integer
# @param B : integer
# @return an integer
def uniquePaths(A, B):
    if A==1 or B == 1:
        return 1
    A = A - 1
    B = B - 1
    if A < B:
        A = A + B
        B = A - B
        A = A - B
        
    res = 1
    j = 1
    for i  in range(A+1, A+B+1):
        res *= i
        res /= j
        j += 1
    return int(res)

A = 3
B = 7
import pdb
pdb.set_trace()
print('uniq paths in grid are:-', uniquePaths(A, B))
