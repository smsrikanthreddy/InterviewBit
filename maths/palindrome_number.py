class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
	    n = len(str(A))
	    A = str(A)
	    left = []
	    right = []
	    for i in A:
	        left.append(i)
	    for j in range(n-1, -1, -1):
	        right.append(A[j])

	    i = 0
	    while i < n:
	        if left[i] != right[i]:
	            return 0
	        i += 1

	    return 1
