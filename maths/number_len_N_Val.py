
def num_len_N(A, B, C):
    n = len(A)
    if n == 0:
        return 0
    counter = 0
    if B < 2:
        print('B is:-', B)
        for i in range(n):
            if A[i] < C:
                counter += 1
    else:
        i = 0
        if (10**(B))< C:
            val = A[i] + (10**(B)) + 10*i
            while val < C:
                for j in range(n):
                    val = A[j] + (10**(B)) + 10*i
                    print('val inside', val)
                    if val < C:
                        counter += 1
                i += 1
        else:
            val = A[i] + (10**(B-1)) + 10*i
            while val < C:
                for j in range(n):
                    val = A[j] + (10**(B-1)) + 10*i
                    print('val inside', val)
                    if val < C:
                        counter += 1
                i += 1
            
                        
    return counter



A = [0, 1, 2, 5]
B = 2
C = 21
A = [0, 1, 5]
B = 1
C = 2
#A = [0]
#B = 1
#C = 5
#A = [0,1,2,5]
#B = 3
#C = 210
A = [0, 1, 2, 5]
B = 2
C = 40
#A = [0, 1, 2, 4, 5]
#B = 2
#C = 300
import pdb
pdb.set_trace()
print('num len N and val less than K:-',num_len_N(A, B, C))
