class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Queues(object):

    def __init__(self, head=None):
        self.head = None
        self.tail = None

    def enqueue(self,new_element):
        if self.head:
            new_element.next = self.head
            self.head = new_element

        else:
            self.head = new_element
            self.tail = new_element
            
    def dequeue(self):
        if self.tail and self.head:
            count  = 0
            current = self.head
            while current.value != self.tail.value:
                current = current.next
            self.tail = current
            return self.tail
        else:
            return None
                
                
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
q = Queues(e1)
q.enqueue(e1)
q.enqueue(e2)
#q.enqueue(e3)
print(q.head.value)
print(q.head.next.value)
print(q.dequeue().value)
print(q.head.value)
print(q.head.next.value)
