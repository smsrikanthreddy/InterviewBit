class Solution:
    def minCostToMoveChips(self, position) -> int:
        n = len(position)
        even, odd = 0, 0
        for val in position:
            if val%2 == 0:
                even += 1
            else:
                odd += 1
        if even==n or odd==n:
            return 0
        return min(even, odd)

sol_obj = Solution()
A = [1, 2, 3]
A = [2,2,2,3,3]
A = [1,1000000000]
A = [1,2,2,2,2]
print(sol_obj.minCostToMoveChips(A))