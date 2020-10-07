def compare( x, y):
    a = int(str(x)+str(y))
    b = int(str(y)+str(x))
    return a, b
    
def find_largest(L, R, A):
    nL = len(L)
    nR = len(R)
    k, j, i = 0,0,0
    while i<nL and j <nR :
        a, b = compare(L[i], R[j])
        if a >= b:
            A[k] = a
            i += 1
        else:
            A[k] = b
            j += 1
        k += 1
    #print('before sending', A[0])
    return A[0]

def largest_number(A):
    l_n = len(A)
    if l_n < 2:
        return A
    mid = int(l_n/2)
    L = A[:mid]
    R = A[mid:]
    largest_number(L)
    largest_number(R)
    #print('L {} R {} A {} sending values '.format(L, R, A))
    find_largest(L, R, A)
    return A[0]

A = [3, 30, 34, 5, 9]
#A = [8, 89]
#A = [3, 30, 34, 5, 9, 6]
print('the largest number is :-', largest_number(A))

'''
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(A)
        def partiation(A, start, end):
            pivot = A[end]
            pindex = start
            for i in range(start, end):
                flag =False
                curr = str(A[i])
                piv = str(pivot)
                if int(curr+piv)>int(piv+curr):
                    flag = True
                if flag:
                    A[i], A[pindex] = A[pindex], A[i]
                    pindex += 1
            A[end], A[pindex] = A[pindex], A[end]
            return pindex
    
        def quickSort(A, start, end):
            if start < end:
                pindex = partiation(A, start, end)
                quickSort(A, start, pindex - 1)
                quickSort(A, pindex + 1, end)
            return A

        xxx = quickSort(A, 0, len(A) - 1)
        yyy = ""
        for i in xxx:
            if i != 0 or yyy:
                yyy+=str(i)
        if not yyy:
            return "0"
        return yyy
'''
'''

from functools import cmp_to_key

class Solution:
	# @param A : tuple of integers
	# @return a strings
	def largestNumber(self, A):
	    ''' When comparing numbers we must pick the one leading
	        to the best concatenated result:
	        787978 > 787879  so 7879 is 'bigger' than 78
	                    but     7879 is 'less' than 788
	    '''
	    
	    # Convert to string once, for proper comparison a+b vs b+a
	    A = map(str, A)
	    key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
	    res = ''.join(sorted(A, key= key, reverse=True))
	    # Must left trim 0, apparently
	    res = res.lstrip('0')
	    return res if res else '0'
'''
'''
Date - 02-Oct-2020

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(A)
        n = len(A)
        def compare(x,y):
            val1 = str(x)+str(y)
            val2 = str(y)+str(x)
            if int(val1)>=int(val2):
                return x,y
            else:
                return y,x
                
        for i in range(n-1):
            for j in range(i+1, n):
                a, b = compare(A[i], A[j])
                A[i] = a
                A[j] = b
        if A[0]==0:
            return 0
        else:
            return "".join([str(val) for val in A])
        
'''