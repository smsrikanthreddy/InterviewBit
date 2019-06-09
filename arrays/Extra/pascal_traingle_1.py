#pascal triangle


def solve(A):
        pascal = []
        def factorail(val):
            if val == 0:
                return 1
            else:
                vals = 1
                for i in range(1,val+1):
                    vals = vals * i
                return vals
        for line in range(0,A):
            small = []
            for i in range(0,line+1):
                small.append(int(factorail(line) / ( factorail(line-i) * factorail(i))))
            pascal.append(small)
        return pascal
		
		
A = 5
import pdb
pdb.set_trace()
print(solve(A))