'''
def min_steps_infinite(A, B):
    prev_x, prev_y, total = A[0], B[0], 0
    for curr_x, curr_y in zip(A, B):
        dx, dy = abs(curr_x - prev_x), abs(curr_y - prev_y)
        if dx < dy:
            total += dy
        else:
            total += dx
        prev_x, prev_y = curr_x, curr_y
    return total
'''
def coverPoints(self, A, B):
        if len(A) <= 1 and len(B) <= 1:
            return 0
        cntr = 0
        i = 0
        for i in range(len(A) - 1):
            cntr += max(abs(A[i + 1] - A[i]), abs(B[i + 1] - B[i]))
        return cntr
    
#A = [0,1,1]
#B = [0,1,2]
A = [ -7, -13 ]
B = [ 1, -5 ]
#A = [ -5, 7, -12, 4, -6, 2, -5, -12, -6, 3, 11, 10, -8, 11, -13, -8, 5, -12, 4, 4 ]
#B = [ -6, 6, -8, -13, -2, -9, -10, -10, -7, -14, 9, -8, -4, 8, 13, -11, 13, 5, 9, 11 ]
print('no of steps are:-', min_steps_infinite(A, B))
