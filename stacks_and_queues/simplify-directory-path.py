
def simplifyPath(A):
        st = []
        dirs = A.split('/')
        for d in dirs:
            if d == '..':
                if st:
                    st.pop()
            elif d and d != '.':
                st.append(d)
        return '/' + '/'.join(st)
'''
def simplifyPath(A):
        names = [] # holds sequence of folder names
        i = 0
        while i < len(A):
            if A[i] == '/':
                
                # find folder name
                i += 1
                j = i
                while i < len(A) and A[i] != '/':
                    i += 1
                name = A[j:i]
                
                # pop or push as required
                if name == '..':
                    if len(names) > 0:
                        names.pop()
                elif name != '.' and name != '':
                    names.append(name)

        return '/' + '/'.join(names)
'''
path = "/home/"#, => "/home"
#path = "/home//foo/"
path = "/a/./b/../../c/"#, => "/c"
#path = "/a//b//c//////d"
#path = "/../"
import pdb
pdb.set_trace()
print(simplifyPath(path))