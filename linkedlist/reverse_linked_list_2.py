# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse(self, head):
        past = None 
        present = head
        tail = head
        while present:
            present.next, past, present = past, present, present.next
        return past, tail
        
        
    def reverseBetween(self, head, m, n):
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
            ohead, whead, wtail = whead, whead.next, wtail.next
        #Step 3#  
        otail, wtail.next = wtail.next, None
        revhead, revtail = self.reverse(whead)
        #Step 4#  
        ohead.next, revtail.next = revhead, otail
        return dummy.next