class Solution:
    def maxPower(self, s: str) -> int:
        #return max(len(list(b)) for a, b in itertools.groupby(s))
        #or
        ans = 1
        i = 0
        for j in range(1, len(s)):
            if s[j] == s[i]:
                ans = max(ans, j-i+1)
            else:
                i = j
        return ans

A = "leetcode"
A = "tourist"
A = "cc"
A = "tlbosjxansrsledgvzkkisafnpubavuu"
s_obj = Solution()
print(s_obj.maxPower(A))