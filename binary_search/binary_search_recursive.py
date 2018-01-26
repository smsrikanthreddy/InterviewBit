#need to implement outside array search term
def binary_search(data,low, high, search_elem):
        mid = int((low + high)/2)
        if search_elem == data[mid]:
            return mid
        elif search_elem < data[mid]:
            return binary_search(data,low, mid - 1, search_elem)
        elif search_elem > data[mid]:
            return binary_search(data, mid + 1, high, search_elem)
        else:
            return -1


a =[1,2,3,4,5,6,7,8]
print('the search element index is:', binary_search(a, 0, len(a), 8))