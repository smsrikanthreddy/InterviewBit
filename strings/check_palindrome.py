def isPalindrome(self, A):
        first = []
        for val in A.lower():
            if val in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]:
                first.append(val)
        cnt = 0
        for val in range(len(first)-1,-1,-1):
            if first[val] != first[cnt]:
                return 0
            cnt += 1
        return 1