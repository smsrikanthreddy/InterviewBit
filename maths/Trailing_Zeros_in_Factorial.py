class Solution:
	# @param A : integer
	# @return an integer
	def trailingZeroes(self, A):
	    sum = 0
	    j = 5
	    while j <= A:
	        sum += A//j
	        j = j * 5
	    return sum
