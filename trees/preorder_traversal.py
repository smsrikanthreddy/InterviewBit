class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        if A is None:
            return A
        ans = []
        stack = []
        stack.append(A)
        while len(stack)>0:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.right != None:
                stack.append(temp.right)
            if temp.left != None:
                stack.append(temp.left)
                
        '''
        while (len(stack) or A != None):
            while A!=None:
                ans.append(A.val)
                if A.right != None:
                    stack.append(A.right)
                A = A.left
                
            if (len(stack) > 0): 
                A = stack[-1] 
                stack.pop()
        '''
        return ans