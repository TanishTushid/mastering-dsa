
class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class DescendingPriorityQueue:
    def __init__(self):
        self.front = None 

    def empty(self):
        return self.front is None
    
    def enqueue(self,value):
        new_node = node(value)
        if self.front is None or value > self.front.value:
            new_node.next = self.front
            self.front = new_node
        else:
            curr = self.front
            while curr.next and curr.next.value >= value:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

    def dequeue(self):
        if self.empty():
            print("queue is empty")
            return
        values = self.front.value
        self.front = self.front.next
        return values
    
    def peek(self):
        if self.empty():
            print("queue is empty")
            return None
        return self.front.value
    
    def display(self):
        if self.empty():
            print("queue is empty")
            return None
        
        curr = self.front
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

#--Test Case--
pq = DescendingPriorityQueue()
pq.enqueue(20)
pq.enqueue(40)
pq.enqueue(10)
pq.enqueue(30)
pq.display()        # 40 -> 30 -> 20 -> 10 -> None

print(pq.peek())    # 40
print(pq.dequeue()) # 40
pq.display()        # 30 -> 20 -> 10 -> None
