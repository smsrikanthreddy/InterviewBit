class Solution():
    # @param A : string
    # @return an integer
    def isValid(self, A):
            Open = "({["
            Close = ")}]"
            stack = []
            for char in A :
                if char in "({[" :
                   stack.append(char)
                else :
                    if len(stack) == 0 :
                        return 0
                    else :
                        top = stack[len(stack) - 1]
                        if Open.index(top) == Close.index(char) :
                            stack.pop()
                        else :
                            return 0
            if len(stack) == 0 :
                return 1
            else :
                return 0



















'''
def push_fnc(elem):
    top= top+1
    stack_list.append(elem)
    
def pop_fnc():
    del stack_list[top]
    top = top - 1
	    	    
def isValid(A):
    operators_start = ['(','{','[']
    operators_end = [')','}',']']
    
    n = len(A)-1
    for i in range(n-1):
        if A[i] in operators_start:
            push_fnc(A[i])
        else:
            if A[i] in operators_end:
                if (len(stack_list)<0) or A[top] != A[i]:
                    return 0
                else:
                    pop_fnc()

    if len(stack_list)<0:
        return 1
    else:
        return 0

A = '(){}[]'
top = -1
stack_list = []
print('balances parenthesis or not ? ', isValid(A))
'''
'''
class Solution:
    # @param A : string
	# @return an integer
	
	def __init__(self):
	    self.top = -1
	    self.stack_list = []
	    
	def push_fnc(self, elem):
	    self.top= self.top+1
	    self.stack_list.append(elem)
	
	def pop_fnc(self):
	    del self.stack_list[self.top]
	    self.top = self.top - 1
	    
	def isValid(self, A):
	    operators_start = ['(','{','[']
	    operators_end = [')','}',']']
	  
	    n = len(A)
	    for i in range(n-1):
	        if A[i] in operators_start:
	            self.push_fnc(A[i])
	        else:
	            if A[i] in operators_end:
	                if (len(self.stack_list)<=0) or (A[self.top] !=  A[i]):
                            print('len :-', len(self.stack_list))
                            print('self.top :-', A[self.top])
                            print('A[i] :-', A[i])
                            return 0
	                else:
	                    self.pop_fnc()
	    if len(self.stack_list)<=0:
	        return 1
	    else:
	        print(self.stack_list)
	        return 0

abc = Solution()
import pdb
pdb.set_trace()
print('output :-', abc.isValid('(){}[]'))
'''
