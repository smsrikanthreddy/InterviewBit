#need to implement outside array search term
def binary_search(data,low, high, search_elem):
    while low <= high:
        mid = int((low + high)/2)
        if search_elem == data[mid]:
            return mid
        elif search_elem < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

#A =[1,2,3,4,5,6,7,8]
A = [ 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10 ]
B = 1
print('the search element index is:', binary_search(A, 0, len(A), B))