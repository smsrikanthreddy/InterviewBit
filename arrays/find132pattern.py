from itertools import accumulate


def find132pattern(nums):
    if len(nums) < 2:
        return False
    i, j, k = 0, 1, 0
    N = len(nums)
    import pdb; pdb.set_trace()
    while i < N-2:
        if i < j:
            if nums[i] < nums[j] and k == 0:
                k = j + 1
            else:
                j += 1
        if i < j < k and k<N and nums[i] < nums[k] and nums[k] < nums[j]:
            print(nums[i], nums[k], nums[j])
        if k == N and j <N:
            j = j+1
            k = j+1
        elif k==N and j==N and i<N-2:
            i += 1
        else:
            k += 1
    return False
A = [-1, 3, 2, 0]
A = [3, 1, 4, 2]
print(list(accumulate(A, min)))
print(find132pattern(A))