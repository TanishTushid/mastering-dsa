# creating a node
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class scll:
    #creating head
    def __init__(self):
        self.head = None
    #traversing 
    def traverse(self):
        if not self.head:
            return "list is empty"
        curr = self.head
        while True:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(head)")
    #insert at beginning
    def insert_head(self,data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self
            while curr.next != self.head:
                curr = curr.next
            new_node.next = self.head
            curr.next = new_node
            self.head = new_node
    #insert at end
    def insert_tail(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while self.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
    
    #insert after value
    def insert_after_value(self,prev,data):
        if not self.head:
            return
        curr = self.head
        while True:
            if curr.data == data:
                new_node = node(data)
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next
            if curr == self.head:
                break
