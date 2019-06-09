class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
		
def addTwoNumbers(a_list, b_list):
        #a_list = []
        #b_list = []
        #while A:
        #    a_list.append(A.val)
        #    A = A.next
        #while B:
        #   b_list.append(B.val)
        #   B = B.next
        sums = []
        if len(b_list) > len(a_list):
           temp = a_list
           a_list = b_list
           b_list = temp

        if len(b_list) != len(a_list):
            carry = 0
            diff = len(a_list) - len(b_list)
            for i in range(0,diff-1):
                if a_list[i] >= 0 and b_list[i] >= 0:
                    if a_list[i] + b_list[i]+carry >= 10:
                        vals = str(a_list[i]+b_list[i]+ carry)
                        sums.append(int(vals[1]))
                        carry  = 1
                    else:
                        vals = a_list[i]+b_list[i] + carry
                        sums.append(vals)
                        carry = 0
            i = diff-1
            while i<len(a_list):
                if a_list[i]+ carry >= 10:
                    vals = str(a_list[i]+ carry)
                    sums.append(int(vals[1]))
                    carry = 1
                else:
                    sums.append(a_list[i]+carry)
                    carry = 0					
                i = i+1
        else:
            carry = 0
            for i in range(0,len(a_list),1):
                if a_list[i] >= 0 and b_list[i] >= 0:
                    if a_list[i] + b_list[i]+ carry >= 10:
                        vals = str(a_list[i]+b_list[i]+ carry)
                        sums.append(int(vals[1])) 
                        carry  = 1
                    else:
                        vals = a_list[i]+b_list[i] + carry
                        sums.append(vals)
                        carry = 0
        
        head = new = ListNode(0)
        i = 0
        while i<len(sums):
            new_val = ListNode(sums[i])
            head.next = new_val
            head = head.next
            i += 1
        head.next = None
        return new.next
		#'''
		
B = [1,2,3,4,5,6,7,8,9]
A = [1,2,3,4,5]
B = [5,6,7,8,9]
A = [1,2,3,4,5]
A = [2,4,3]
B = [5,6,4]
#A = [5,6,3]
#B = [8,4,2]
#A = [7,5,9,4,6]
#B = [8,4]
import pdb
pdb.set_trace()
print(addTwoNumbers(A,B))

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        a_list = []
        b_list = []
        while A:
            a_list.append(A.val)
            A = A.next
        while B:
           b_list.append(B.val)
           B = B.next
        flag = False
        if len(b_list) > len(a_list):
           temp = a_list
           a_list = b_list
           b_list = temp
           flag = True
        sums= []
        if len(b_list) != len(a_list):
            carry = 0
            diff = len(a_list) - len(b_list)
            for i in range(0,diff-1):
                if a_list[i] >= 0 and b_list[i] >= 0:
                    if a_list[i] + b_list[i]+carry >= 10:
                        vals = str(a_list[i]+b_list[i]+ carry)
                        sums.append(int(vals[1]))
                        carry  = 1
                    else:
                        #vals = a_list[i]+b_list[i] + carry
                        #sums.append(vals)
                        #carry = 0
                        if a_list[i]+b_list[i] + carry >= 10:
                            vals = str(a_list[i]+ carry)
                            sums.append(int(vals[1]))
                            carry = 1
                        else:
                            sums.append(a_list[i]+carry)
                            carry = 0  
                else:
                    sums.append(a_list[i]+carry)
                    carry = 0 
            i = diff-1
            while i<len(a_list):
                if a_list[i]+ carry >= 10:
                    vals = str(a_list[i]+ carry)
                    sums.append(int(vals[1]))
                    carry = 1
                else:
                    sums.append(a_list[i]+carry)
                    carry = 0                   
                i = i+1
        else:
            carry = 0
            for i in range(0,len(a_list),1):
                if a_list[i] >= 0 and b_list[i] >= 0:
                    if a_list[i] + b_list[i]+ carry >= 10:
                        vals = str(a_list[i]+b_list[i]+ carry)
                        sums.append(int(vals[1])) 
                        carry  = 1
                    else:
                        #vals = a_list[i]+b_list[i] + carry
                        #sums.append(vals)
                        #carry = 0
                        if a_list[i]+b_list[i] + carry >= 10:
                            vals = str(a_list[i]+ carry)
                            sums.append(int(vals[1]))
                            carry = 1
                        else:
                            sums.append(a_list[i]+carry)
                            carry = 0 
                        
        head = new = ListNode(0)
        i = 0
        while i<len(sums):
            new_val = ListNode(sums[i])
            head.next = new_val
            head = head.next
            i += 1
        head.next = None
        return new.next
                
'''