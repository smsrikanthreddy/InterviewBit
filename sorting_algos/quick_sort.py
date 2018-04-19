    
def partition(A, start, end):
    pivot = A[end]
    pIndex = start
    for i in range(start, end):
        if A[i] <= pivot:
            tmp = A[i]
            A[i] = A[pIndex]
            A[pIndex] = tmp
            pIndex = pIndex + 1
            
    tmp = A[pIndex]
    A[pIndex] = A[end]
    A[end] = tmp
    
    return pIndex

def quick_sorting(A, start, end):
    if start < end:
        pIndex = partition(A, start, end)
        quick_sorting(A, start, pIndex-1)
        quick_sorting(A, pIndex+1, end)
    return A


A = [7, 2, 1, 6, 8, 5, 3, 4]
A = [7, 4, 3, 2, 1, 5, 3]
end = len(A)-1
start = 0
import pdb
pdb.set_trace()
print('quick sorted list is :- ', quick_sorting(A, start, end))
