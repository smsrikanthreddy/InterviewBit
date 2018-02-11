def maxset(A):
	    i = 0;
	    maxi = -1;
	    index = 0;
	    a = []
	    
	    while i < len(A):
	        while i < len(A) and A[i] < 0:
	            i+=1
	        l = []
	        index = i
	        while i < len(A) and A[i] >= 0:   
	            l.append(A[i])
	            i+=1
	        
	        if (sum(l) > maxi):
	            a = l
	            maxi = sum(l)
	    
	    return a

A = [1,2,5,-7, 2, 3]
A = [ 336465782, -278722862, -2145174067, 1101513929, 1315634022, -1369133069, 1059961393, 628175011, -1131176229, -859484421 ]
print('max non neg subarray:-', maxset(A))
