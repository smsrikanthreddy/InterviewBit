class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        # for i in range(len(A)):
        # print('first one:-  i={}, A[i]={}, abs(A[i])={}, A[abs(A[i])]={}'.format(i, A[i], abs(A[i]), A[abs(A[i])]))
        #    if A[abs(A[i])] >= 0:
        # A[abs(A[i])] = A[abs(A[i])] - A[abs(A[i])]
        # print('first one:-  i={}, A[i]={}, abs(A[i])={}, A[abs(A[i])]={}'.format(i, A[i], abs(A[i]), -A[abs(A[i])]))
        #        A[abs(A[i])] = -A[abs(A[i])]
        # print('final Array {} :-', A)
        #    else:
        #        return i

        arr_size = len(A)
        for i in range(arr_size):
            A[A[i] % arr_size] = A[A[i] % arr_size] + arr_size;

            # print("The repeating elements are : ");
        for i in range(arr_size):
            if (A[i] >= arr_size * 2):
                # print(i, " ");
                return i
        return -1
