class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        outs = []
        for i in range(1,A+1):
            if i%15==0:
                outs.append("FizzBuzz")
            elif i%3==0:
                outs.append("Fizz")
            elif i%5 == 0:
                outs.append("Buzz")
            else:
                outs.append(i)
        return outs
