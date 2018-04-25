def primesum(A):
    #sieve of Eratosthenes
    prime_no = [True] * (A + 1)
    
    prime_no[0] = False
    prime_no[1] = False

    for i in range(2, int(A**0.5)+1):
        if prime_no[i]:
            j = 2
            while i*j < A+1:
                prime_no[i*j] = False
                j += 1
                
    for n in range(2, len(prime_no)+1):
        if prime_no[n] and prime_no[A-n]:
            return [n, A-n]
    

A = 15
#A = 16777214
#A = 100
#A = 4
print('the prime sum elems are:-', primesum(A))
