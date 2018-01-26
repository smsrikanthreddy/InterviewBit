
def matrix_search(arr, x):
    m, n = 2,2
    r = 0
    c = 0
    print(arr)
    while x >= arr[r][c]:
        if arr[r][c] == x:
            return r,c
        elif r<=m:
            r = r+1
        elif r==2 and c<=n:
            c = c+1
        else:
            return 'not found'
    r = r - 1
    c = c + 1
    while x >= arr[r][c]:
        if arr[r][c] == x:
            return r,c
        elif c <=n:
            c = c + 1
        else:
            return 'not found'
        
def searchMatrix(A, B):
        m = len(A)
        n = len(A[0])
        print('m {} and n {}'.format(m,n))
        l, h = 0, m * n - 1
        while l <= h:
            mid = l + (h - l) // 2
            if A[mid // n][mid % n] == B:
                return 1
            elif A[mid // n][mid % n] < B:
                l = mid + 1
            else:
                h = mid - 1
        return 0



a = [[1,2,3],[4,5,6],[7,8,9]]
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
a = [[3],[29],[36],[63],[67],[72],[74],[78],[85]]
x = 63
print('element found at:-', matrix_search(a, x))
print('element found :-', searchMatrix(a,x))
