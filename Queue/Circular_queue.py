

class circular_queue:
    def __init__(self,size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1)% self.size == self.front
    
    def is_empty(self):
        return self.front == -1
    
    def enqueue(self,value):
        if ((self.rear +1) % self.size == self.front):
            print("queue is full")
        elif (self.front == -1):
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1)%self.size
            self.queue[self.rear] = value

    def dequeue(self):
        if self.front==-1:
            print("queue is empty")
        elif self.front == self.rear:
            removed = self.queue[self.front]
            self.front = self.rear = -1
            return removed
        else:
            removed = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return removed
    
    def peek_front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]
    
    def peek_rear(self):
        if self.is_empty():
            print("queue is empty")
            return None
        return self.queue[self.rear]
    
    def display(self):
        if self.front == -1:
            print("queue is empty")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()

cq = circular_queue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()          # Output: 10 20 30 40

print(cq.dequeue())   # Output: 10
print(cq.peek_front()) # Output: 20
print(cq.peek_rear())  # Output: 40

cq.enqueue(50)
cq.enqueue(60)
cq.display()          # Output: 20 30 40 50 60

cq.enqueue(70)        # Output: Queue is Full
