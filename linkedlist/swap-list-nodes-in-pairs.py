# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A is None:
            return None
        head = A
        while A != None and A.next != None:
            temp = A.val
            A.val = A.next.val
            A.next.val = temp
            #A, A.next.val = A.next.val, A.val
            A = A.next.next
        return head