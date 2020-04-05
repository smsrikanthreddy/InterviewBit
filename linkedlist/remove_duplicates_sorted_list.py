# Definition for singly-linked list. 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A.next==None:
            return A
        head = A
        while head:
            if head.next!=None and head.val == head.next.val:
                head.next = head.next.next
            else:   
                head = head.next
        return A