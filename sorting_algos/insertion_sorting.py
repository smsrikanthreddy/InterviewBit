
def insertion_sort(A, A_n):

    for i in range(1, A_n):
        value = A[i]
        temp = i

        while temp > 0 and A[temp-1] > value:
            A[temp] = A[temp-1]
            temp = temp -1
        A[temp] = value
        
    return A



A = [1, 7, 4, 2, 5, 3]
A_n = len(A)
print('inserion sorted list is:-', insertion_sort(A, A_n))
