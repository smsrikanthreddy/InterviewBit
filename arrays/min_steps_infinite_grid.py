import math

def max_steps_infinite(A, B):
    if len(A) == 0 and len(A) != len(B):
        return 0
    value = 0
    for i in range(0, len(A)):
        value += max(abs(A[i] - A[i-1]), abs(B[i] - B[i-1]))
        return value



#A = [0,1,1]
#B = [0,1,2]
#A = [ -7, -13 ]
#B = [ 1, -5 ]
