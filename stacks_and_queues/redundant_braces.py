class Solution:
    	# @param A : string
	# @return an integer
    def braces(self, A):
        braces = 0
        for char in A :
            if char == '(' :
                braces += 1
            elif char in "*/+-" :
                braces -= 1
            if braces < 0 :
                braces = 0
        if braces == 0 :
            return 0
        else :
            return 1    
