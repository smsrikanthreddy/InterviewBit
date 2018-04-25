def romanToInt(A):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50,'C':100,'D':500,'M':1000}
        old = roman_dict[A[0]]
        val1 = 0
        new_old = 0
        for ro in range(len(A)):
            val = roman_dict[A[ro]]
            if old < val:
                val1 = val1 + val
                new_old = new_old + old
            else:
                val1 = val1 + val
            old = val
        val1 = val1 - 2*new_old
        return val1




A = "XLX"
A = "XXX"
A = "MDCCCIV"
#A = "MMCDLXXV"
print('roman ', A, ' integers :- ', romanToInt(A))
