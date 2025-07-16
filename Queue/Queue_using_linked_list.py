# Queue using linked list

class node:
    def __init__(self, value):
        self.data = value
        self.next = None
class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        new_node = node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front == None:
            return "Empty"
        else:
            self.front = self.front.next

    def peek_front(self):
        if self.front ==None:
            return "empty"
        else :
            return self.front.data
    
    def peek_rear(self):
        if self.front == None:
            return "empty"
        else:
            return self.rear.data

    def is_empty(self):
        if self.front == None:
            return "Empty"
        
    def size(self):
        curr = self.front
        counter = 0
        while curr != None:
            counter += 1
            curr = curr.next
        return counter

    def traverse(self):
        curr = self.front
        while curr != None:
            print(curr.data)
            curr = curr.next


q = queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.traverse()
q.dequeue()
q.traverse()
print(q.is_empty())
print(q.peek_front())
print(q.peek_rear())