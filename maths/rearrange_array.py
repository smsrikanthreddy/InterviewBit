
def rearrange_array(A):
    n = len(A)
    for i in range(n):
        A[i] += (A[A[i]]%n)*n
    print('1-step array is:-', A)
    for i in range(n):
        A[i] = A[i]//n

    return A





A = [3, 2, 0, 1]
#A = [4,2,0,1,3]
import pdb; pdb.set_trace()
print('rearranged array is:-', rearrange_array(A))
