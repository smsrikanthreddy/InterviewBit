def partition(A, start, end):
    pivot = A[end]
    pIndex = start
    for i in range(start, end):
        if A[i] <= pivot:
            temp = A[i]
            A[i] = A[pIndex]
            A[pIndex] = temp
            pIndex += 1
            
    temp = A[end]
    A[end] = A[pIndex]
    A[pIndex] = temp
    return pIndex
	
def quick_sort(A, start, end):
    if start < end:
        pIndex = partition(A, start, end)
        quick_sort(A, start, pIndex-1)
        quick_sort(A, pIndex+1, end)
    
def subUnsort(A):
    n = len(A)-1
    first = -1
    last = -1
    
    for i in range(n):
        if A[i] > A[i+1]:
            first = i
            break

    if first == -1:
        return -1
    
    for j in range(n, -1, -1):
        if A[j] < A[j-1]:
            last = j
            break
        
    if last == -1:
        return -1
    
    min_val = min(A[first:last+1])
    max_val = max(A[first:last+1])
    #print('min val', min_val, max_val)
    
    print('unsorted Array is :-', A[first:last+1])
    quick_sort(A, first, last)
    #print('sorted sub array com:-', A)
    for i in range(0, first):
        if A[i] > min_val:
            temp = A[first]
            A[first] = A[i]
            A[i] = temp
                 
    for j in range(last, n):
        if A[j] < A[last]:
            temp = A[j]
            A[j] = A[last]
            A[last] = temp
            
    print('total complete sorted array :-', A)
    return first, last

    

A = [0, 2, 20, 30, 25, 40, 32, 31, 35, 50, 60] #3, 8
#A = [1, 2, 3] #-1
A = [ 2, 2, 3, 4, 4, 4, 6, 7, 8, 8, 12, 17, 16, 16, 20, 17, 18, 20, 16 ] #11, 18
print('max sub array is:-', subUnsort(A))
