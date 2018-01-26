'''
def sqrt(A):
    i = 1
    min = 1
    max = 1
    while i < A:
        min = max
        i = max + 10
        max = i
        i = i * i
        
    while min <= max:
        j = min    
        if j * j == A:
            return j
        if j * j < A:
            min = j + 1
        if j * j > A:
            max = j -1
        if j * j < A and (j+1)*(j+1) > A:
            return j

A = 122
#A = 11
#A = 273189320
#import pdb
#pdb.set_trace()
print('sqrt is:-', sqrt(A))
'''
#with more optimized binary search

def binsearch(start, end, A):
    while start <= end:
        mid = (start+end)//2
        if mid * mid == A:
            return mid
        if mid*mid < A:
            ans = mid
            start = mid+1
        else:
            end = mid-1
    return ans
        
def sqrt(A):
    start = 0
    end = A
    if A==0 or A==1:
        return A
    else:
        return binsearch(start, end, A)

print('sqrt is:-', sqrt(11))
