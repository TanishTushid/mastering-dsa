# circular queue using linked list 

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circularqueueliskedlist:
    def __init__(self):
        self.front = None
        self.rear = None 

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = node(data)
        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        value = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        return value
    
    def display(self):
        if self.is_empty():
            print("queue is empty")
            return 
        print("queue: ", end=' ')
        temp = self.front
        while True:
            print(temp.data,end=" ")
            temp = temp.next
            if temp == self.front:
                break
        print()

cq = circularqueueliskedlist()

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()          # Output: 10 20 30 40

print(cq.dequeue())   # Output: 10

cq.enqueue(50)
cq.enqueue(60)
cq.display()          # Output: 20 30 40 50 60

cq.enqueue(70)       