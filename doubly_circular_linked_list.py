

class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class doublylinkedlist:
    def __init__(self):
        self.head = None

    def insert_from_head(self, data):
        new_node = node(data)
        if self.head is None:          #empty list
            new_node.next = new_node    #point to self
            new_node.prev = new_node    
            self.head = new_node        # set as head
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = self.head.prev = new_node
            self.head = new_node
            
    def insert_at_tail(self,data):
        new_node = node(data)
        if self.head is None:
            # First node in the list
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def insert_after_value(self,target,data):
        if self.head is None:
            print("list is empty")
            return 
        curr = self.head
        while True:
            if curr.data == target:
                new_node = node(data)
                new_node.next = curr.next
                new_node.prev = curr
                curr.next.prev = new_node
                curr.next = new_node
                return
            curr = curr.next
            if curr == self.head:
                break
            print(f"value {target} not found")

    def delete_from_head(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head

    def delete_from_tail(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            new_tail = tail.prev
            new_tail.next = self.head
            self.head.prev = new_tail

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            if temp.data == value:
                if temp == self.head:
                    self.delete_from_head()
                elif temp.next == self.head:
                    self.delete_from_tail()
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"Value {value} not found")

    def search(self, value):
        if self.head is None:
            return False
        temp = self.head
        while True:
            if temp.data == value:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def count_nodes(self):
        if self.head is None:
            return 0
        count = 1
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        return count

    def traverse_forward(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        print("Forward:", end=" ")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def traverse_backward(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head.prev
        print("Backward:", end=" ")
        while True:
            print(temp.data, end=" ")
            temp = temp.prev
            if temp.next == self.head:
                break
        print()

dll = doublylinkedlist()

dll.insert_from_head(10)
dll.insert_at_tail(20)
dll.insert_at_tail(30)
dll.insert_after_value(20, 25)
dll.traverse_forward()     # Output: 10 20 25 30
dll.traverse_backward()    # Output: 30 25 20 10

dll.delete_by_value(25)
dll.traverse_forward()     # Output: 10 20 30

dll.delete_from_head()
dll.traverse_forward()     # Output: 20 30

dll.delete_from_tail()
dll.traverse_forward()     # Output: 20

print("Found:", dll.search(20))  # True
print("Count:", dll.count_nodes())  # 1
