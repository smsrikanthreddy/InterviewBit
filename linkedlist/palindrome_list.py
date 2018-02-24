
class Solution:
    # @param A : head node of linked list
    # @return an integer
    def reverseList(self, A):
        present = A
        past = None
        future = A.next
        while present != None:
            future = present.next
            present.next = past
            past = present
            present = future
        return past


    def length(self, A):
        counts = 0
        B = A
        while B and B.next:
            A = A.next
            B = B.next.next
            counts += 1
        return counts, A

    def lPalin(self, A):
        if A == None:
            return 1
        if A.next == None :
            return 1
    
        mid_index, mid = self.length(A)
        rev_list = self.reverseList(mid)

        for i in range(0, mid_index):
            if rev_list.val == A.val:
                rev_list = rev_list.next
                A = A.next
            else:
                return 0
        return 1


'''




class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head

    def append(self, elem):        
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = elem
        else:
            self.head = elem

    def length(self, A):
        counts = 0
        A = self.head
        B = A
        while B and B.next:
            A = A.next
            B = B.next.next
            counts +=1
        return counts, A

    def reverseList(self, A):
        present = A
        past = None
        future = A.next
        while present != None :
            future = present.next
            present.next = past
            past = present
            present = future
        return past

    def create_list(self):
        e1 = ListNode(1)
        e2 = ListNode(2)
        e3 = ListNode(3)
        e4 = ListNode(2)
        e5 = ListNode(1)
        
        ll = LinkedList(e1)
        ll.append(e2)
        ll.append(e3)
        #ll.append(e4)
        #ll.append(e5)
        
        return ll

def lpalin():
    ll1 = LinkedList()
    ll = ll1.create_list()
    #print('1 st element', l1.val, 'sec elem', l1.next.val)
    #print('mid element is at:- ', ll.length(ll))
    mid_index, mid = ll.length(ll)
    print('mid index value is:-', mid_index)
    rev_list = ll.reverseList(mid)
    print('rev_list {} '.format(rev_list.val))
    #print('mid counter value is {} and mid last val {}'.format(counter, mid.val))
    p1 = ll.head.val
    #print('ll values :-', ll.head.val, p1)
    for i in range(0, mid_index):
        #p1 = ll.head.val
        if rev_list.val == p1:
            print('mid val {} '.format(rev_list.val))
        else:
            print('not mached')
            
        rev_list = rev_list.next
        if ll.head.next:
            ll = ll.head.next
        print('ll values inside {}:-', ll.val)
        p1 = ll.val
        
lpalin()
''' 
    
    
