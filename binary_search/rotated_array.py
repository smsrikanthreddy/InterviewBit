class Solution:
    # @param A : tuple of integers
    # @return an integer
    def nooftimesrotated(self, A):
        N = len(A)
        low = 0
        high = N-1
        while (low <=high):
            if A[low] <= A[high]:
                return low
            mid = int((low+high)/2)
            next1 = mid+1%N
            prev1 = (mid-1)%N
            if A[mid] <= A[next1] and A[mid] <= A[prev1]:
                return mid
            if A[mid] <= A[high]:
                high = mid - 1
            if A[mid] >= A[low]:
                low = mid + 1
        retrurn -1

    def findMin(self, A):
        return A[self.nooftimesrotated(A)]
    
A = [15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12]
#A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
model = Solution()
print('min value is :-', model.findMin(A))
