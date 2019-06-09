### Merge Sort
A = [2,3,4,3,4]


def merge(L,R,A):
	nL = len(L)
	nR = len(R)
	k,j,i = 0,0,0
	while (i<nL and j<nR):
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i+1
		else:
			A[k] = R[j]
			j = j+1
		k += 1
	while (i<nL):
		A[k] = L[i]
		i +=1
		k +=1
	while (j < nR):
		A[k] = R[j]
		j += 1
		k += 1
	return A
	
def mergesort(A):
	
	n = len(A)
	if n < 2:
		return A
	mid = int(n/2)
	left = A[:mid]
	right = A[mid:]
	mergesort(left)
	mergesort(right)
	merge(left, right, A)
	return A
	
print("initial array",A)		
mergesort(A)
print("sorted array", A)

'''
def maximumGap(A):
        n = len(A)
        if n == 1:
            return 0
        left = [0]*n; left[0] = A[0]
        for i in range(1, n):
            left[i] = min(left[i-1], A[i])
        right = [0]*n; right[-1] = A[-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], A[i])
        i = 0; j = 0; ans = -1
        while i < n and j < n:
            if right[j] >= left[i]:
                ans = max(ans, j-i)
                j += 1
            else:
                i += 1
        return ans

A = [3,5,4,2]
import pdb
pdb.set_trace()
print(maximumGap(A))	
'''
