# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sums = 0

        '''
        ### O(n) + O(1)
        #while head:
        #    sums = 2*sums + head.val
        #    head = head.next

        ### O(n2) + 
        pow_2 = 0
        temp = head
        lst_val = 0
        while temp:
            lst_val += 1
            temp = temp.next
        lst_val = lst_val -1
        while head:
            sums = sums + (head.val * (2 ** lst_val))
            head = head.next
            lst_val = lst_val - 1

        '''

        while head:
            sums = sums << 1 | head.val
            head = head.next
        return sums
