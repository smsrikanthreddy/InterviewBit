class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        minNum = A[0]
        stack = []
        for i in range(len(A)):
            if A[i] <= minNum:
                stack.clear
            while len(stack) != 0 and A[i] <= stack[-1]:
                stack.pop()
            if len(stack) == 0:
                stack.append(A[i])
                minNum = A[i]
                A[i] = -1
            else:
                stack.append(A[i])
                A[i] = stack[-2]
        return A
