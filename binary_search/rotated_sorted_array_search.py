#not the most efficient one, need to improve
def search(A, B):
    n = len(A)
    low = 0
    high = n
    i = 0
    pivot = -1
    while i < n-1:
        if A[i] > A[i+1]:
            pivot = i
            i = n
        else:
            i += 1
    if pivot != -1:
        A1 = A[low:pivot+1]
        A2 = A[pivot+1:high]
        if A1[0] <= B:
            A = A1
        elif A2[-1] <= B:
            A = A2
    low = 0
    high = len(A)-1
    while low <= high:
        mid = int((low+high)/2)
        if A[mid] == B:
            return mid
        if A[mid] < B:
            low = mid + 1
        if A[mid] > B:
            high = mid -1
    return -1

A = [ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
B = 202
#A = [1, 5, 7, 22, 33]
#B = 1
import pdb
pdb.set_trace()
print('search elem at pos:-', search(A, B))
