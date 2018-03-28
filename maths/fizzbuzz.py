class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
	    #n = len(A)
	    ans = []
	    for i in range(1, A+1):
	        if i%3 == 0 and i%15 != 0:
	            ans.append('Fizz')
	        elif i%5 == 0 and i%15 != 0:
	            ans.append('Buzz')
	        elif i%15 == 0:
	            ans.append('FizzBuzz')
	        else:
	            ans.append(i)
	    return ans
