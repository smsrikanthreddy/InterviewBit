#insertion sort
def insertion_sort(A):
    for i in range(1, len(A)):
        temp = A[i]
        j = i
        while j>0 and A[j-1]>temp:
            A[j] = A[j-1]
            j -= 1
        A[j] = temp
    return A

if __name__ == "__main__":
    A = [6,5, 4, 7, 4, 2, 1]
    A = [ 5 , 66 , 68 , 42 , 73 , 25 , 84 , 63 , 72 , 20 , 77 , 38 , 8 , 99 , 92 , 49 , 74 , 45 , 30 , 51 , 50 , 95 , \
          56 , 19 , 31 , 26 , 98 , 67 , 100 , 2 , 24 , 6 , 37 , 69 , 11 , 16 , 61 , 23 , 78 , 27 , 64 , 87 , 3 , 85 , \
          55 , 22 , 33 , 62 ]
    print(insertion_sort(A))