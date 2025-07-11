class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def traverse(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next

    def peek(self):
        if (self.is_empty()):
            return "stack empty"
        else:
            return self.top.data
    def pop(self):
        if(self.is_empty()):
            return "stack empty"
        else:
            self.top = self.top.next

s = stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.is_empty())  # Output: False
s.traverse()
s.pop()
s.peek()
s.traverse()

