# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def insert(self, A, values):
	    temp = A
	    while A:
	        A = A.next
	    print('before A values', A.val)
	    A = values
	    A = A.next
	    print( ' A values', A.val)
	    return A
	
    def partition(self, A, B):
        head = A
        h1 = temp1 = ListNode(0)
        h2 = temp2 = ListNode(0)
        
        while head:
            if head.val < B:
                temp1.next = head
                temp1 = temp1.next
            else:
                temp2.next = head
                temp2 = temp2.next
            head = head.next
        
        temp2.next = None
        temp1.next = h2.next
        return h1.next
