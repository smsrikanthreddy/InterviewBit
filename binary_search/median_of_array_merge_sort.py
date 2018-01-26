def merge(arr, l, m, r):

    n1 = m - l + 1
    n2 = r - m
    
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l+i]

    for j in range(0, n2):
        R[j] = arr[m+1+j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:

        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k +=1
        
    while i < n1:
        arr[k] = L[i]
        i +=1
        k += 1
        
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    
def merge_sort(arr, l, r):
    if(l < r):
        m = int((l+(r-1))/2)
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

        
def findMedianSortedArrays(A, B):

    arr = A+B
    n = len(arr)
    if n < 0:
        return 0
    elif n == 1:
        return arr[n-1]
    elif n == 2:
        return (arr[0]+arr[1])/2.0
    else:
        merge_sort(arr, 0, n-1)
        arr_n = len(arr)
        
        if arr_n%2 == 0:
            mid = int(arr_n/2)
            avg = (arr[mid-1]+arr[mid])/2.0
            return avg
        else:
            mid = int(arr_n/2)
            return arr[mid]

            
A = [1,4,5]
A = [1,4]
B = [2,3, 6]
B = [2,3]
A = [ -50, -41, -40, -19, 5, 21, 28 ]
B = [ -50, -21, -10 ]
A = [ -50, -41, -40, -19, 5, 21, 28 ]
B = [ -50, -21, -10 ]
A = [0,1,2,3]
B = [0,1]
A = [0, 23]
B = []
#merge_sort(arr, 0, n-1)
print('median is:-', findMedianSortedArrays(A, B))
