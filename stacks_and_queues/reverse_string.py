class Solution:
	# @param A : string
	# @return a strings
	def reverseString(self, A):
	    stack = ""
	    for i in reversed(range(len(A))):
	        stack = stack + A[i]
	    return stack
