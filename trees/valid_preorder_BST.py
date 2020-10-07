'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def chk(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        root = A[0]
        left = [i for i in A if i<root]
        right = [i for i in A if i>root]
        
        root_left = self.chk(left)
        root_right = self.chk(right)
        
        if root >= 1:
            return 1
        else:
            return 0
            
    def solve(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        root = A[0]
        for val in A[1:]
'''
def solve(self, A):
        root = -1
        stack = []
        for i  in range(len(A)):
            if A[i] < root:
                return 0
            while len(stack)>0 and stack[-1] < A[i]:
                root = stack.pop()
                
            stack.append(A[i])
        return 1

A = [2, 4, 3]
print(solve(A))