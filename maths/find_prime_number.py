class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        primes = {}
        for i in range(A+1):
            primes[i] = 1
        primes[0] = 0
        primes[1] = 0
        
        for i in range(2,int(A**0.5)+1):
            if primes[i] == 1:
                j = 2
                while i*j <= A:
                    primes[i*j] = 0
                    j += 1
        primes1 = []
        for k,v in primes.items():
            if v == 1:
                primes1.append(k)
        return primes1