def asteroidCollision(asteroids):
    stack = []
    #import pdb; pdb.set_trace()
    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
        else:
            while len(stack) != 0 and stack[-1] > 0 and stack[-1] < abs(asteroid):
                stack.pop()
            if len(stack) == 0 or stack[-1] < 0:
                stack.append(asteroid)
            elif abs(stack[-1]) == abs(asteroid):
                stack.pop()
    print(stack)

A = [-1, -2, 1, 3]
A = [5, 10, -15]
A = [10, 2, -5]
A = [-2,-1,1,2]
asteroidCollision(A)