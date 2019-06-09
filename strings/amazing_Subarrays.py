def solve(self, A):
        n = len(A)
        cnt = 0
        summup = 0
        for val in A:
            if val in ["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                summup = summup + (n-cnt)
            cnt += 1
        
        return summup % 10003