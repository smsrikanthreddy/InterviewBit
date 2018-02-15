
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

def length(list):
    temp = list.head
    ll_len = 0
    while (temp != None):
        ll_len += 1
        temp = temp.next
    return ll_len

def findMergePoint(A, B):
                
    m = length(A)
    n = length(B)
    d = n - m
    print('length of m is {} and n is {}'.format(m, n))

    if m > n :
        temp = Node()
        temp = A
        A = B
        B = temp
        d = m - n
        
    A = A.head
    B = B.head
    
    for i in range(0, d):
        B = B.next

    while(A!= None and B!= None):
        if(A == B):
            return A.data
        A = A.next
        B = B.next
    return NULL

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

# Start setting up a LinkedList
l1 = LinkedList(n1)
l1.append(n2)
l1.append(n3)
l1.append(n4)
print(l1.head.data)

n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

l2 = LinkedList(n5)
l2.append(n6)
l2.append(n3)
l2.append(n7)

print('merge point is:-', findMergePoint(l1, l2))


'''
def length(A):
    res = 0
    while A:
        A = A.next
        res += 1
    return res

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        
        m = length(A)
        n = length(B)
        
        # Make A the shortest one
        if m > n:
            m, n, A, B = n, m, B, A
        
        # Advance B so the tail has same length as A
        for _ in range(n-m):
            B = B.next
        
        while A and A is not B:
            A, B = A.next, B.next
        
        return A
'''
