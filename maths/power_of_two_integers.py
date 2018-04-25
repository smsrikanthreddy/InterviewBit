class Solution:
    # @param A : integer
	# @return an integer
    def isPower(self, A):
        if A==1:
            return 1
        for i in range(2,A):
            count = 0
            j = i
            A_1 = A
            while A_1 != 1 and A_1%j == 0:
                A_1 = A_1//j
                count += 1
            if A_1 == 1:
                return 1
        return 0

#https://www.ideserve.co.in/learn/check-if-a-number-can-be-expressed-as-x-raised-to-power-y-set-1
