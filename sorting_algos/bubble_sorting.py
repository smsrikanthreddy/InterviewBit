
def bubble_sort(A, A_n):

    for k in range(1, A_n-1):

        flag =0
        for i in range(0, A_n-1):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                flag=1
        if flag==0:
            break
    return A


A = [2, 7, 4, 1, 5, 3]
A_n = len(A)

print('bubble sorted list is:-', bubble_sort(A, A_n))
