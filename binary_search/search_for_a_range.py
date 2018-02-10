

def search_range(A, a, b):
    low = 0
    high = len(A)

    while low <=high:
        mid = int((low+high)/2)
        if A[mid] == a:
            low = mid
        elif A[mid] < a and A[mid+1]> a:
            low = mid+ 1
            low_range = mid
        elif A[mid] > a and A[mid-1]< a:
            high = mid-1
            low_range=mid
        elif A[mid] < a:
            low = mid + 1
        elif A[mid] > a:
            high = mid - 1
            
    new_arr = A[low:]
    arr = []
    for val in new_arr:
        if val <= b:
            arr.append(val)
    return arr



#A = [1,2,3,4,5,6,50,56,57,58]
#a = 49
#b = 59
A = [5, 7, 7, 8, 8, 10]

print('the range numbers are:-', search_range(A, a, b))
