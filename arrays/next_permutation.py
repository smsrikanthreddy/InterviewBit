def partition(A, start, end):
    pivot = A[end]
    pIndex = start
    for i in range(start, end):
        if A[i] <= pivot:
            temp = A[i]
            A[i] = A[pIndex]
            A[pIndex] = temp
            pIndex = pIndex + 1
            
    temp = A[pIndex]
    A[pIndex] = A[end]
    A[end] = temp
        
    return pIndex
        
def quick_sort(A, start, end):
    if start < end:
        pIndex = partition(A, start, end)
        quick_sort(A, start, pIndex-1)
        quick_sort(A, pIndex+1, end)
        
            
def nextPermutation(A):
    n = len(A)-1
    i_count = 0
    for i_val in range(n, -1, -1):
        if A[i_val] < A[i_val-1]:
            i_count += 1
            continue
        else:
            break
            
    if i_count == 0:
        A = self.quick_sort(A, 0, n)
        return A
            
    f = A[i_count-1]
    low = 0
    count1 = 0
    for j in range(n, i_count, -1):
        if f < A[j]:
            if count1 == 0:
                low = A[j]
                count1 += 1
            elif low > A[j]:
                count1 += 1
                low = A[j]
                    
    temp = A[i_count-1]
    A[i_count-1] = A[n-1-count1]
    A[n-1-count1] = temp
    #A1 = A[i_count:]
    #print(A1)
    quick_sort(A, i_count, n)
    
    # sort array 
    return A

A = [1, 5, 8, 4, 7, 6, 5, 3, 1]
import pdb
pdb.set_trace()
print('array is :-', nextPermutation(A))

'''
class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    
    def partition(self, A, start, end):
        pivot = A[end]
        pIndex = start
        for i in range(start, end):
            if A[i] <= pivot:
                temp = A[i]
                A[i] = A[pIndex]
                A[pIndex] = temp
                pIndex = pIndex + 1
                
        temp = A[pIndex]
        A[pIndex] = A[end]
        A[end] = temp
        
        return pIndex
        
    def quick_sort(self, A, start, end):
        if start < end:
            pIndex = self.partition(A, start, end)
            self.quick_sort(A, start, pIndex-1)
            self.quick_sort(A, PIndex+1, end)
            
    def nextPermutation(self, A):
        n = len(A)-1
        count = 0
        i_count = 0
        for i_val in range(n, -1, -1):
            if A[i_val] < A[i_val-1]:
                i_count += 1
                continue
            else:
                #temp = A[i_val - 1]
                #A[i_val - 1] = A[i_val]
                #A[i_val] = temp
                #count += 1
                break
            
        m = n - i_count
        for j in range(n, m, -1):
            if A[j] < A[j-1]:
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
                
        
        if count == 0:
            A = self.quick_sort(A, 0, n)
        # sort array 
        return A
'''
