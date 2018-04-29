class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
	    if A == 0 :
	        return B 
	    return self.gcd(B%A, A)
