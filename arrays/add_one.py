'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)
        A[n-1] += 1
        carry = A[n-1]/10
        A[n-1] = A[n-1]%10

        for val in range(n-2,-1,-1):
            if carry == 1:
                A[val] += 1
                carry = A[val]/10
                A[val] = A[val]%10
        if carry == 1:
            A.insert(0,1)

        while True:
            if A[0] == 0:
                del A[0]
            else:
                return A
        return A

'''
'''
def plusOne(A):
    if len(A) == 0:
        return A
    if A == [0]:
        return A[0]+1
    N = len(A)
    str_val = ""
    carry = 1
    for val in range(N, -1, -1):
        #print(val)
        if val == 9:
            carry = 1
            str_val = str_val + str(0)
        else:
            str_val = str_val + str(val + carry)
            carry = 0
            str
    str_val = int(str_val)
    rev = 0

    while (str_val > 0):
        a = str_val % 10
        rev = rev * 10 + a
        str_val = str_val // 10

    return rev
'''

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