class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        a = [[] for i in range(A)]
        for i in range(A):
            for j in range(i+1):
                if ( j<i ):
                    if (j == 0):
                        a[i].append(1)
                    else:
                        a[i].append(a[i-1][j] + a[i-1][j-1]) 
                elif ( j == i):
                    a[i].append(1)
        return a
'''
class Solution:
    # @param A : integer
	# @return a list of list of integers
    def binomialCoeff(self, n, k) :
        res = 1
        if (k > n - k) :
            k = n - k
        for i in range(0 , k) :
            res = res * (n - i)
            res = res // (i + 1)
        return res
        
    def generate(self, A):
        result = []
        for line in range(0, A) :
            res1 = []
            for i in range(0, line + 1) :
                res1.append(self.binomialCoeff(line, i))
            result.append(res1)
        return result
         
'''
