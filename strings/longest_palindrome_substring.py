
#arr = ['a']* 8
def long_palin(A, i, j):
    if i==j:
        #arr[i] = A[i]
        #print(arr[i])
        return 1
    if A[i]==A[j] and i+1==j:
        arr[i] = A[i]
        arr[j] = A[j]
        return 2
    if A[i]==A[j]:
        arr[i] = A[i]
        arr[j] = A[j]
        return long_palin(A, i+1, j-1)+2
    print(arr)
    return max(long_palin(A, i, j-1), long_palin(A, i+1, j))
        


A = "BBABCBCAB"
n = len(A)
#A = 'geeksforgeeks'
#n = len(A)
arr = ['a']*n
print('the longest palindrom substring is:-', long_palin(A, 0, n-1))
