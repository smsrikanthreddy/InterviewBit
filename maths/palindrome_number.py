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
	        
	    i = 0
	    j = n -1
	    while i < n:
	        if left[i] != left[j]:
	            return 0
	        i += 1
	        j -= 1

	    return 1
