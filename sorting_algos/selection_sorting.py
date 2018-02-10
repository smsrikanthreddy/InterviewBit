
def selection_sort(A, A_n):
    
    for i in range(0, A_n-2):
        imin = i
        for ji in range(i+1, A_n):#in python it is i+1 to A_n-1 elements
            if A[ji] < A[imin]:
                imin = ji
        temp = A[i]
        A[i] = A[imin]
        A[imin] = temp
    return A



A = [2,7,4,1,5,3]
A_n = len(A)
import pdb
pdb.set_trace()
print('selection sorted list are:-', selection_sort(A, A_n))
