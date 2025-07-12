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
            data = self.top.data
            self.top = self.top.next
            return data

def text_editor(text,pattern):

    u = stack()
    r = stack()

    for i in text:
        u.push(i)

    for i in pattern:
        if i == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)
            
    res = ""
    while (not u.is_empty()):
        res = u.pop() + res
    print(res)

text_editor("kolkata","uurruur")
