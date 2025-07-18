# priority queue using linked list

class node:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority
        self.next = None

class prioityqueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return "empty"
        
    def enqueue(self, value, priority):
        new_node = node(value,priority)
        if self.head is None or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next and curr.next.priority <= priority:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return None
        removed_node = self.head
        self.head = self.head.next
        return (removed_node.value, removed_node.priority)
    
    def peek(self):
        if self.is_empty():
            print("queue is empty")
            return None
        return (self.head.value,self.head.priority)

    def display(self):
        if self.is_empty:
            print("queue is empty")
        else:
            curr = self.head
            print("priority queue:")
            while curr:
                print(f"value: {curr.value}, priority: {curr.priority}")
                curr = curr.next

# --- Test Code ---
pq = prioityqueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)

pq.display()

print("Peek:", pq.peek())
print("Dequeue:", pq.dequeue())
pq.display()