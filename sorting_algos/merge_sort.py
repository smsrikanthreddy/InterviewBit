
def merge(L, R, A):
    nL = len(L)
    nR = len(R)
    k, j, i = 0,0,0
    while i<nL and j <nR :
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i<nL:
        A[k] = L[i]
        i += 1
        k += 1
    while j<nR:
        A[k] = R[j]
        j += 1
        k += 1
    return A


def mergesort(A):
    import pdb
    pdb.set_trace()
    
    l_n = len(A)
    if l_n < 2:
        return A
    mid = int(l_n/2)
    L = A[:mid]
    R = A[mid:]
    mergesort(L)
    mergesort(R)
    merge(L, R, A)
    return A

A = [23, 32, 4, 5, 6, 76]
A = [3, 30, 34, 5, 9]
print('merge sort sorted list is :-', mergesort(A))
