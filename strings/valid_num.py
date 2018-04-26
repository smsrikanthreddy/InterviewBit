class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        A = A.strip()
        n = len(A)
        if n < 1:
            return 0
        if n ==1:
            if A in ['0', '1','2', '3','4','5','6','7','8','9']:
                return 1
            else:
                return 0
        if A[-1] == '.':
            return 0
     
        if (A.count('-') == 1 and A[0] != '-') or A.count('.') > 1 :
            return 0
            
        num_alpha = ['0', '1','2', '3','4','5','6','7','8','9','e','-','.']
        fix = 'abcd'
        fix2 = 'bcd'
        for i in range(n):
            #print(i)
            if A[i] not in num_alpha:
                #print(A[i])
                return 0
            else:
                old = A[i]
                if old == '.':
                    fix2 = '.'
                if old=='e':
                    fix = old
                if fix == 'e' and old =='.':
                    return 0
                if A[i] == '.' and A[i+1] == 'e':
                    return 0
        return 1
            
