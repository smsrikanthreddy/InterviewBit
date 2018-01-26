"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None        
        
class Stack(object):

    def __init__(self, head=None):
        self.head = head

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        current = self.head
        if self.head:
            new_element.next = current
            self.head = new_element
        else:
            self.head = new_element

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        
        if self.head:
            current = self.head
            #new_current = self.head.next
            self.head = self.head.next
            return current
        else:
            return None
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.head.value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)
