'''
def maximumGap(A):
    if len(A) == 0:
        return -1
    # arr[i][j] = max distance starting from i and including up to j
    index = list(range(len(A)))
    print(index)
    index.sort(key=lambda x: A[x])
    print('sorted array is:-', index)
    largest_distance = 0
    max_index_from_i = [index[-1]] * len(A)
    i = len(A) - 2
    while i >= 0:
        max_index_from_i[i] = max(max_index_from_i[i+1], index[i])
        i -= 1
    for i in range(len(A) - 1):
        largest_distance = max(largest_distance, max_index_from_i[i] - index[i])
    if largest_distance <= 0:
        return 0
    else:
        return largest_distance
'''
from operator import itemgetter
# @param A : tuple of integers
# @return an integer
def maximumGap(A):
    Max = 0
    L = []
    for i in range(len(A)) :
        L.append([A[i], i])
    print('first L is:-', L)
    L.sort(key = itemgetter(0))
    print('L after sort:-', L)
    Max = -1
    for i in range(len(L) - 1, -1, -1) :
        Max = max(Max, L[i][1])
        L[i][0] = Max
    Max = 0
    for i in range(len(L)) :
        Max = max(Max, L[i][0]- L[i][1])
    return Max

A = [-1, -1, 2]
A = [ 3, 2, 1 ]
import pdb
pdb.set_trace()
print('max distance :-', maximumGap(A))

'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        if n == 1:
            return 0
        left = [0]*n; left[0] = A[0]
        for i in range(1, n):
            left[i] = min(left[i-1], A[i])
        right = [0]*n; right[-1] = A[-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], A[i])
        i = 0; j = 0; ans = -1
        while i < n and j < n:
            if right[j] >= left[i]:
                ans = max(ans, j-i)
                j += 1
            else:
                i += 1
        return ans
'''
