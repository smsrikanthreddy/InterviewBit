def merge(L,R,A):
    nl = len(L)
    nr = len(R)
    k,i,j = 0,0,0
    while (i<nl and j<nr):
        if L[i] <= R[j]:
           A[k] = L[i]
           i += 1
        else:
           A[k] = R[j]
           j += 1
        k += 1
    while i<nl:
        A[k] = L[i]
        i += 1
        k += 1
    while j<nr:
        A[k] = R[j]
        j += 1
        k += 1
	
    return A
	
def merge_sort(A):
    n  = len(A)
    if n <=1:
	    return A
    mid = n/2
    left = A[:mid]
    right = A[mid:]
    merge_sort(left)
    merge_sort(right)
    A = merge(left,right,A)
    return A

def sort_list(A):
    A1 = list(map(lambda x:x[0],A))
    print(merge_sort(A1))


A = [(1,2),(4,5),(3,2),(3,5)]
print(sort_list(A))