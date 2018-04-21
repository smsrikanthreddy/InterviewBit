class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
	    if len(A) == 0:
	        return 0
	    val = A.strip().split(" ")
	    return len(val[-1])
