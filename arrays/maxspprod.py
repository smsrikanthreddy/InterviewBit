#MAXSPROD
'''
def Maxspprod(A):
    L = []
    R = []
    n = len(A)
    for i,val1 in enumerate(A):
        #flag_L = False
        flag_R = False
        max_j = 0
        for j in range(i):
            if A[j]>val1:
                max_j = j
                
        for j in range(i+1,n):
            if A[j]>val1:
                R.append(j)
                flag_R = True
                break
        #if max_j:
        L.append(max_j)
        if flag_R == False:
            R.append(0)
    out = [a*b for a,b in zip(L,R)]
    return max(out)
'''

def Maxspprod(A):
        if len(A)<3:
            return 0
        stack = []
        max_prod = 0
        for i in range(len(A)-1, -1, -1):
            while stack and A[i] > A[stack[-1]]:
                stack.pop()
                if stack:
                    max_prod = max(max_prod, i*stack[-1])
            stack.append(i)  
            if max_prod > 0 and stack[-1] <= len(A)/2:
                break
        return max_prod%1000000007

A = [ 5, 9, 6, 8, 6, 4, 6, 9 , 5, 4, 9 ]
#A = [5,4,3,4,5]
import pdb
pdb.set_trace()
print(Maxspprod(A))