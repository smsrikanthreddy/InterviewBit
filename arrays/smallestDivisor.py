import math
class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        import pdb; pdb.set_trace()
        small_div = 0
        for x in range(threshold, 1, -1):
            sums = 0
            for val in nums:
                sums = sums+ math.ceil(val/x)
            if sums <= threshold:
                if x<small_div:
                    small_div = x
            return small_div


s_d = Solution()
array = [1,2,5,9]
threshold = 6
print(s_d.smallestDivisor(array, threshold))