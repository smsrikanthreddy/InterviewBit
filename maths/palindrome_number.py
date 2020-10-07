class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        A = str(A)
        int_lst = []
        for i in A:
            int_lst.append(i)
        i = 0
        j = len(str(A)) - 1
        while i < j:
            if int_lst[i] != int_lst[j]:
                return 0
            i += 1
            j -= 1
        return 1
