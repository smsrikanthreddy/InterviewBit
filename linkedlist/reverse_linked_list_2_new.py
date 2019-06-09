class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head):
    past = None 
    curr = head
    tail = head
    while curr:
        tail = curr.next
        curr.next = past 
        past = curr
        curr = tail
    return past, tail
        
        
def reverseBetween(head, m, n):
        if m >= n:
            return head
        #Step 1#    
        ohead = dummy = ListNode(0)
        whead = wtail = head
        dummy.next = head
        for i in range(n-m):
            wtail = wtail.next
        #Step 2#  
        for i in range(m-1):
            ohead = whead
            whead = whead.next
            wtail = wtail.next
        #Step 3#  
        otail = wtail.next
        wtail.next = None
        revhead, revtail = reverse(whead)
        #Step 4#  
        ohead.next = revhead
        revtail.next = otail
        out = []
        dummy = dummy.next
        while dummy:
            out.append(dummy.val)
            dummy = dummy.next
        return out
		
A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
C = ListNode(9)
C1 = ListNode(4)
C2 = ListNode(5)
C3 = ListNode(6)
C4 = ListNode(7)
C5 = ListNode(8)

A.next = B
B.next = C
C.next = C1
C1.next = C2
C2.next = C3
C3.next = C4
C4.next = C5

print(A.val)
print(A.next.val)
print(A.next.next.val)
print(A.next.next.next.val)
print(A.next.next.next.next.val)
print(A.next.next.next.next.next.val)
print(A.next.next.next.next.next.next.val)
print(A.next.next.next.next.next.next.next.val)
m = 3
n = 6
import pdb
pdb.set_trace()
print('rev in b/w', reverseBetween(A,m,n))

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def reverse(self, A,cnt,n):
        curr = A
        future = A
        past = None
        while curr and cnt<=n:
            future = curr.next
            curr.next = past
            past = curr
            curr = future
            cnt += 1
        return past, future
    def reverseBetween(self, head, m, n):
        #Step 1#    
        ohead = dummy = ListNode(0)
        whead = wtail = head
        dummy.next = head
        cnt = 1
        for i in range(n-m):
            wtail = wtail.next
            cnt += 1
        #Step 2#  
        for i in range(m-1):
            ohead = whead
            whead = whead.next
            wtail = wtail.next
        #Step 3#  
        otail = wtail.next
        wtail.next = None
        revhead, revtail = self.reverse(whead, cnt, n)
        #Step 4#  
        ohead.next = revhead
        revtail.next = otail
        dummy = dummy.next
        return dummy
'''