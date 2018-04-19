'''
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
def binomialCoeff(n1, k) :
    res = 1
    if (k > n1 - k) :
        k = n1 - k
    for i in range(0 , k) :
        res = res * (n1 - i)
        res = res // (i + 1)
    return res
        
def generate(A):
    result = []
    for line in range(0, A) :
        res1 = []
        for i in range(0, line + 1) :
            res1.append(binomialCoeff(line, i))
        result.append(res1)
    return result

A = 5
import pdb
pdb.set_trace()
print('pascal traingle :-', generate(A))
