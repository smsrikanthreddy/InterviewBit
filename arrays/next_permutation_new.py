### Next permutation
def next_permutation(A):
    #A = list(A)
    n = len(A)
    ## case 1
    ## if the digits are in descending order
    flag_dsc = False
    flag_asc = False
    for i in range(0,n-1):
        if A[i] >= A[i+1]:
            continue
        else:
            flag_dsc = True
    if flag_dsc != True:
        print('hi')
        #B = A
        return sorted(A)
    
    ## case 2, asc order
    for i in range(n-1):
        if A[i]<=A[i+1]:
            continue
        else:
            flag_asc=True
    if flag_asc != True:
        temp = A[0]
        A[0] = A[n-1]
        A[n-1] = temp
        return A
    ## case 3
    small_great = -1
    for j in range(n-1,-1,-1):
        if A[j] > A[j-1]:
            index = j-1
            for i in range(index+1,n):
                if A[index] < A[i]:
                    if small_great == -1:
                        small_great = i
                    elif A[i] < A[small_great]:
                        small_great = i
            if small_great <0:
                return A
            else:
                temp = A[index]
                A[index] = A[small_great]
                A[small_great] = temp
                sliced_list = A[index+1:n]
                sliced_list.sort()
                ind = index
                for val in sliced_list:
                    A[ind+1] = val
                    ind = ind+1
                return A
        else:
            continue
                    

A = '54321'
A = '534976'
A =  [ 251, 844, 767, 778, 658, 337, 10, 252, 632, 262, 707, 506, 701, 475, 410, 696, 631, 903, 516, 149, 344, 101, 42, 891, 991 ]
A = [3,2,1]
print('input is:-', A)
import pdb
pdb.set_trace()
print(next_permutation(A))


'''
class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
            
                
    def nextPermutation(self, A):
        #A = list(A)
        n = len(A)
        ## case 1
        ## if the digits are in descending order
        flag_dsc = False
        flag_asc = False
        for i in range(0,n-1):
            if A[i] >= A[i+1]:
                continue
            else:
                flag_dsc = True
        if flag_dsc != True:
            return sorted(A)
        
        ## case 2, asc order
        for i in range(n-1):
            if A[i]<=A[i+1]:
                continue
            else:
                flag_asc=True
        if flag_asc != True:
            temp = A[0]
            A[0] = A[n-1]
            A[n-1] = temp
            return A
        ## case 3
        small_great = -1
        for j in range(n-1,-1,-1):
            if A[j] > A[j-1]:
                index = j-1
                for i in range(index+1,n):
                    if A[index] < A[i]:
                        if small_great == -1:
                            small_great = i
                        elif A[i] < A[small_great]:
                            small_great = i
                if small_great <0:
                    return A
                else:
                    temp = A[index]
                    A[index] = A[small_great]
                    A[small_great] = temp
                    sliced_list = A[index+1:n]
                    sliced_list.sort()
                    ind = index
                    for val in sliced_list:
                        A[ind+1] = val
                        ind = ind+1
                    return A
            else:
                continue
'''



