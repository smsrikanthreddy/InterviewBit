# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sort_list(self, A):
        for i in range(1, len(A)):
            temp = A[i]
            j = i
            while j > 0 and A[j - 1] > temp:
                A[j] = A[j - 1]
                j -= 1
            A[j] = temp
        return A

    def insertionSortList(self, A):
        head = A
        if head is None:
            return head
        new_head = head

        arr_lst = []
        while new_head:
            arr_lst.append(new_head.val)
            new_head = new_head.next
        sort_lst = self.sort_list(arr_lst)
        new_head = head
        while new_head:
            new_head.val = sort_lst.pop(0)
            new_head = new_head.next
        return head
'''
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, elem):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = elem
        else:
            self.head = elem
        return self.head

def linked_list():
    e1 = Node(1)
    e2 = Node(5)
    e3 = Node(2)
    e4 = Node(0)

    ll = LinkedList(e1)
    head = ll.insert(e2)
    head = ll.insert(e3)
    head = ll.insert(e4)

    #print(head.value)
    return head

head = linked_list()

def insertion_sort_list(head):
    res = Node(head.value)
    temp = head.next
    while temp:
        temp1 = res
        prev = None
        while temp1 != None and temp1.value <= temp.value:
            prev = temp1
            temp1 = temp1.next
        if prev == None:
            new = Node(temp.value)
            new.next = temp1
            res = new
        else:
            new = Node(temp.value)
            prev.next = new
            new.next = temp1
            temp = temp.next
    return res

def print_result(head):
    head = insertion_sort_list(head)
    while head:
        print('val sorted:-', head.value)
        head = head.next
import pdb
pdb.set_trace()
print('insertion sort linkedlist is:-', print_result(head))

'''





