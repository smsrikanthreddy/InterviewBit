
def rev_int(A):
    A = int(A)
    if A > 2**31 :
        return 0
    neg = False
    #to handle negative sign case
    if A < 0:
        A = str(A)
        A = int(A[1:])
        neg = True
            
    rev_num = 0
    while A > 0:
        rev_num = (rev_num*10) + (A%10)
        A = int(A/10)
        if rev_num == 0:
            rev_num = 0
    if neg==True:
        rev_num = -rev_num
    if rev_num < -(2**31):
        return 0
    return rev_num


A = 1234560
A = -12334560
A = 1234e127
import pdb
pdb.set_trace()
print('rev integer is:-', rev_int(A))
