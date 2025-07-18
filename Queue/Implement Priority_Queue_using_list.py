#Implement Priority Queue using list


class priorityqueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, value, priority):
        new_item = (priority, value)
        self.queue.append(new_item)
        self.queue.sort()      #ascending based on priority

    def dequeue(self):
        if self.is_empty():
            print("queue is empty. cannot dequeue.")
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            print("queue is empty.")
            return None
        return self.queue[0]
    
    def display(self):
        if self.is_empty():
            print("queue is empty.")
        else:
            print("priority queue:")
            for priority, value in self.queue:
                print(f"value: {value}, priority: {priority}")

#test case
pq = priorityqueue()

pq.enqueue("Task A",3)
pq.enqueue("Task B",1)
pq.enqueue("Task C",2)

pq.display()
print("peek:",pq.peek())
print("dequeue:",pq.dequeue())
pq.display()