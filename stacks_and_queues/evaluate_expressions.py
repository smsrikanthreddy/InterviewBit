# Evaluate expression - stacks

def evalute_exp(A):
    stack = []
    for val in A:
        if val not in ['*','+','-','/']:
            stack.append(val)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if val == '+':
                vals = int(val2) + int(val1)
                stack.append(vals)
            elif val == '-':
                vals = int(val2) - int(val1)
                stack.append(vals)
            elif val == '*':
                vals = int(val2) * int(val1)
                stack.append(int(vals))
            elif val == '/':
                vals = int(val2) / int(val1)
                stack.append(int(vals))
            else:
                print('not found')
    return int(stack[0])


A = '123*+'
A = "231*+9-"
A = "100200+2/5*7+"
A = "22/"
import pdb
pdb.set_trace()
print(evalute_exp(A))