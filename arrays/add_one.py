

def plusOne(A):
    for val in range(len(A)-1,-1,-1):
        if A[val] == 9:
            A[val] = 0
        else:
            A[val] += 1
            while True:
                if A[0] == 0:
                    del A[0]
                else:
                    return A
            return A

    A = [1] + A
    return A
			
			
#A = [1,2,3]
#A = [9,9,9]
A = [2, 5, 6, 8, 6, 1, 2, 4, 5 ]
A = [0]
#A =  [ 1, 9, 9, 9, 9, 9, 9 ]
#A = [ 1, 1, 1, 3, 2, 1, 1, 2, 5, 9, 6, 5 ]
import pdb
pdb.set_trace()
print(plusOne(A))


'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, a):
        t = list(map(str, a))
        p = ''.join(t)
        num = int(p) + 1
        num = str(num)
        temp = []
        for i in range(len(num)):
            temp.append(int(num[i]))

        return temp
'''
'''
n = len(a) 
   
    # Add 1 to last digit and find carry 
    a[n-1] += 1
    carry = a[n-1]/10
    a[n-1] = a[n-1] % 10
   
    # Traverse from second last digit 
    for i in range(n-2,-1,-1): 
        if (carry == 1): 
           a[i] += 1
           carry = a[i]/10
           a[i] = a[i] % 10
          
    # If carry is 1, we need to add 
    # a 1 at the beginning of vector 
    if (carry == 1): 
      a.insert(0, 1) 
'''