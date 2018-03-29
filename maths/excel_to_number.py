class Solution:
    # @param A : string
	# @return an integer\
    def titleToNumber(self, A):
        n = len(A)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = 0
        for i in range(n):
            num += (alphabet.index(A[i]) + 1) *  (26 ** (n - i - 1) )
        return num
