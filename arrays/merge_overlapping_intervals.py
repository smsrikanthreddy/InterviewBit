def merge(A):
    stack = []
    #A.sort(key=lambda i: i[0])
    A.sort()
    for value in A:
        if len(stack) == 0:
            stack.append(value)
        else:
            if stack[-1][1] >= value[1]:
                continue
            elif stack[-1][1]<value[1] and stack[-1][1]>=value[0]:
                val = stack[-1][0]
                stack.pop()
                stack.append((val,value[1]))
            else:
                stack.append(value)
    return stack
	
A = [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6)]
#A = [(6,8),(1,9),(2,4),(4,7)]
A = [ (5, 28), (7, 70), (54, 93), (5, 98), (46, 70), (42, 63), (5, 91), (30, 49), (36, 57), (31, 95), (86, 88), (9, 90), (5, 53), (42, 62), (14, 100), (59, 75), (32, 100), (5, 79), (31, 31), (7, 42), (13, 47), (44, 87), (61, 83), (100, 100), (96, 98), (47, 51), (34, 44), (6, 53), (30, 92), (50, 64), (37, 57), (49, 67), (2, 67), (36, 50), (55, 100), (54, 78), (58, 70), (2, 37), (13, 54), (7, 60), (16, 79), (35, 78), (17, 57), (16, 84), (60, 80), (10, 54), (54, 59), (62, 85), (7, 37), (31, 99), (40, 41), (4, 99), (28, 45), (27, 71), (14, 64) ]
import pdb
pdb.set_trace()
print(merge(A))