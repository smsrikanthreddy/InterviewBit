class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
	    n = len(A)
	    left = [0] * n
	    right = [0] * n
	    water = 0
	    
	    left[0] = A[0]
	    for i in range(1,n):
	        left[i] = max(A[i], left[i-1])
	    right[n-1] = A[n-1]
	    for i in range(n-2, -1, -1):
	        right[i] = max(A[i], right[i+1])
	    
	    for i in range(0,n):
	        water += min(left[i], right[i]) - A[i]
	    return water
