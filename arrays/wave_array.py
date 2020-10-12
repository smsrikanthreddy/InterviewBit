
def partition(A, m, n):
    pivot = A[n]
    pIndex = m
    for i in range(m, n):
        if A[i] <= pivot:
            temp = A[i]
            A[i] = A[pIndex]
            A[pIndex] = temp
            pIndex = pIndex + 1
    temp = A[pIndex]
    A[pIndex] = A[n]
    A[n] = temp
    return pIndex

def quick_sort(A, m, n):
    if m<n:
        pIndex = partition(A, m, n)
        quick_sort(A, m, pIndex-1)
        quick_sort(A, pIndex+1, n)
    return A

def wave_array(A):
    m, n = 0, len(A)
    arr = quick_sort(A, m, n-1)
    print('sorted array :', arr)
    # Swap adjacent elements
    for i in range(0,n-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

    '''
    def wave(self, A):
        A.sort()

        def swap(i, j):
            tmp = A[k]
            A[k] = A[k + 1]
            A[k + 1] = tmp

        k = 0
        while k + 1 < len(A):
            swap(A[k], A[k + 1])
            k += 2
        return A
'''
A = [3, 6, 5, 10, 7, 20]
A = [ 5, 1, 3, 2, 4 ]
print('wave array is:-', wave_array(A))
