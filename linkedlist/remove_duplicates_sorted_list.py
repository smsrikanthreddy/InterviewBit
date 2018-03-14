# Definition for singly-linked list. 
# class ListNode: 
#      def __init__(self, x): 
#          self.val = x 
#          self.next = None

class Solution(object):
    
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return []
        cur = head
        while cur != None:
            while cur.next != None and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
