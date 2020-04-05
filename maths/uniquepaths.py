class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def factorial(self,val):
	    fact = 1
	    for v in range(1,val+1):
	        fact = fact * v
	    return fact
	    
	def uniquePaths(self, A, B):
	    if (B > A):
	        return self.uniquePaths(B, A)
        if (A < 1 or B < 1):
            return 0
        m = A-1
        n = B-1
        val = self.factorial(m+n)/(self.factorial(m)*self.factorial(n))
        return int(val)