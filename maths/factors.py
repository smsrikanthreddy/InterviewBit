'''
def allFactors(A):
        factors = []
        import math
        if A<=1:
           return A
        i = 1
        while i <= math.sqrt(A): 
            if A%i == 0:
                factors.append(i)
                if i!=math.sqrt(A):
                    factors.append(int(A/i))
            i += 1
        second = []
        first = []
        n = len(factors)
        if n%2 != 0:
            for i in range(n-1):
                if i%2 == 0:
                    first.append(factors[i])
                else:
                    second.append(factors[n-1-i])
        else:
            for i in range(n):
                if i%2 == 0:
                    first.append(factors[i])
                else:
                    second.append(factors[n-i])
        return first+second
'''
import math
def allFactors(A):
	factors = []
	factors2 = []
	    # brute force
	for x in range(1, int(math.sqrt(A))+1):
	    d, m = divmod(A, x)
	    if m == 0:
	        factors.append(x)   # sorted
	        if d != x:
	            factors2.append(d) # reverse sort
	               
	    factors2.reverse()
	return factors + factors2
'''
def allFactors(self, A):
        
        L=[]
        for i in range(1,int(sqrt(A))+1):
            if(A%i==0):
                L.append(int(i))
                if(i!=sqrt(A)):
                    L.append(int(A/i))
        L.sort()
        return(L)
'''
A = 36
A = 85463
#A = 1
import pdb
pdb.set_trace()
print(allFactors(A))