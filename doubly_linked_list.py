
class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None
    
    def insert_head(self,data):
        new_node = node(data)
        if self.head:
            self.head.prev = new_node
            self.head.next = self.head
        self.head = new_node

    def insert_tail(self,data):
        new_node = node(data)
        if not self.head:
            self.head = None
            return " empty"
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_node(self,key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if not temp:
            return
        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    def display_forword(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backword(self):
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print(None)



dll = dll()
dll.insert_head(10)
dll.insert_tail(20)
dll.insert_tail(30)
dll.display_forword()    
dll.display_backword()   
dll.delete_node(10)
dll.display_forword()

