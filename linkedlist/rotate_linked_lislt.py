class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        nhead = head
        vals = []
        while nhead:
            vals.append(nhead.val)
            nhead = nhead.next
        if k %len(vals) == 0: return head
        k = k%len(vals)
        for i in range(k):
            vals.insert(0,vals[len(vals)-1-i])
        vals = vals[:len(vals)-k]
        nhead = head
        i = 0
        while nhead:
            nhead.val = vals[i]
            nhead = nhead.next
            i += 1
        return head
'''
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head        
        node, n = head, 0
        while node.next:
            node = node.next
            n += 1
        
        n = n+1
        k = k%n
        
        node.next = head
        node = head
        for _ in range(n - (k + 1)):
            node = node.next
        head = node.next
        node.next = None
        return head
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head        
        node, n = head, 1
        while node.next:
            node = node.next
            n += 1
        k = k%n
        p1, p2 = head, head
        for i in range(0, k):
            p2 = p2.next;
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = head
        newHead = p1.next
        p1.next = None
        return newHead