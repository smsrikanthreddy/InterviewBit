# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, A):
	    curr = A
	    prev = None
	    future = A
	    while curr:
	        future = curr.next
	        curr.next = prev
	        prev = curr
	        curr = future
	    return prev

