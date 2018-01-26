'''
Simple Method: The simplest method to solve this problem is to store all the elements of the given matrix in an array of size r*c. Then find the median element in this array.This seems to be the simplest method but it would take extra memory.
Time Complexity = O(r*c)
Auxiliary Space = O(r*c)

An efficient approach for this problem is to use binary search algorithm. The idea is that for a number to be median there should be exactly (n/2) numbers which are less than this number. So, we try to find the count of numbers less than all the numbers. Below is the step by step algorithm for this approach:
Algorithm:

First we find the minimum and maximum elements in the matrix. Minimum element can be easily found by comparing the first element of each row, and similarly the maximum element can be found by comparing the last element of each row.
Then we use binary search on our range of numbers from minimum to maximum, we find the mid of the min and max, and get count of numbers less than our mid. And accordingly change the min or max.
For a number to be median, there should be (r*c)/2 numbers smaller than that number. So for every number, we get the count of numbers less than that by using upper_bound() in each row of matrix, if it is less than the required count, the median must be greater than the selected number, else the median must be less than or equal to the selected number.

'''

def upper_bound(nums, target):
    l_l, r_r = 0, len(nums) - 1
    while l_l <= r_r:
        mid = int(l_l + (r_r - l_l) / 2)
        if nums[mid] > target:
            r_r = mid - 1
        else:
            l_l = mid + 1
    return l_l

def findMedian(A):
    min = A[0][0]
    max = 0
    for i in range(3):
        if A[i][0] < min:
            min = A[i][0]
        if A[i][2] > max:
            max = A[i][2]
    desired = int((3*3+1)/2)
    while(min<max):
        mid = int(min+(max-min)/2)
        count = 0
        for i in range(3):
            indx = upper_bound(A[i], mid)
            count += indx
        if count < desired:
            min = mid+1
        else:
            max = mid
    return min

#A = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]
A = [[11,14,16],[11,12,16],[13,17,19]]
#mat = np.array(A)
print('median is at :', findMedian(A))
