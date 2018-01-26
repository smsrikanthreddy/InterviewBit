#range = min and max position of search element in the sorted array


def search_range(nums, target):
    i = 0
    j = len(nums)-1
    ret = []

    if nums[i] == target == nums[j]:
            return [i,j]

    while(i<j):
        mid = int((i+j)/2)
        if nums[mid] < target:
            i = mid + 1
        else:
            j = mid
            
    if nums[i] != target:
        ret.append(-1)
    else:
        ret.append(i)

    j = len(nums)-1
    while(i<j):
        mid = int((i+j)/2) + 1
        if nums[mid] > target:
            j = mid - 1
        else:
            i = mid
            
    if nums[j] != target:
        ret.append(-1)
    else:
        ret.append(j)

    return ret




#A = [5, 7, 7, 8, 8, 8, 10]
#a = 8
#A = [1]
#a = 1
#A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
#a = 10
A = [ 4, 7, 7, 7, 8, 10, 10 ]
a = 3
print('index value are:-', search_range(A, a))
