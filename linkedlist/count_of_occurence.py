class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def bs(self, A, B, low, high, result, searchFirst):
        while low<=high:
            mid = (low+high)//2
            if A[mid]==B:
                result = mid
                if searchFirst:
                    high = mid-1
                else:
                    low = mid+1
            elif A[mid]>B:
                high = mid-1
            else:
                low = mid + 1
        return result
        
    def findCount(self, A, B):
        low = 0
        high = len(A)-1
        result = -1
        first_val = self.bs(A, B, low, high, result, True)
        if first_val==result:
            return 0
        else:
            result = -1
            last_val = self.bs(A, B, low, high, result, False)
            return (last_val - first_val+1)
        
        