
def convert(A, B):
    n = len(A)
    a_dict = {}
    j1 = 0
    while j1 < n:
        i = 0
        while i<B and j1<n:
            if i not in a_dict:
                a_dict[i] = [A[j1]]
            else:
                #print(j1, A[j1])
                a_dict[i].append(A[j1])
            i += 1
            j1 += 1
        Flag=True
        B1 = B - 2
        while  B1 > 0 and j1 < n and Flag==True:
            #print('B1 is:-', B1)
            a_dict[B1].append(A[j1])
            B1 -= 1
            j1 += 1
    val = ""
    for i in a_dict.values():
        for j in i:
            val = val + j
    return val



A =  "PAYPALISHIRING"
B =  3
A = "ABCD"
B = 2
import pdb
pdb.set_trace()
print('after conversion :', convert(A, B))
