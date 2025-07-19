# minimum priority queue

class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class AscendingPriorityQueue:
    def __init__(self):
        self.front = None

    def empty(self):
        return self.front is None
    
    def enqueue(self,value):
        # case 1: queue is empty or new value is smallest
        new_node = node(value)
        if self.front is None or value < self.front.value:
            new_node.next = self.front
            self.front = new_node
        else:
            # insert in corrent sorted position
            curr = self.front
            while curr.next and curr.next.value <= value:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

    def dequeue(self):
        if self.empty():
            print("queue is empty")
            return None 
        value = self.front.value 
        self.front = self.front.next
        return value
    
    def peek(self):
        if self.empty():
            print("Queue is empty")
            return None 
        return self.front.value
    
    def display(self):
        if self.empty():
            print("queue is empty")
            return 
        curr = self.front
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")


# test case
pq = AscendingPriorityQueue()
pq.enqueue(30)
pq.enqueue(10)
pq.enqueue(20)

pq.display()

print(pq.peek())
print(pq.dequeue())
pq.display()