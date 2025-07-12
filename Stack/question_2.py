class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def size(self):
        return self.count

    def traverse(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def pop(self):
        if self.is_empty():
            return "stack empty"
        else:
            data = self.top.data
            self.top = self.top.next
            self.count -= 1
            return data

# Matrix representation
l = [
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 0],  # Person 2 is the celebrity
    [0, 0, 1, 0]
]

def find_the_celeb(l):
    s = stack()

    for i in range(len(l)):
        s.push(i)

    while s.size() >= 2:
        i = s.pop()
        j = s.pop()

        if l[i][j] == 1:
            # i knows j → i is not celeb
            s.push(j)
        else:
            # i doesn't know j → j is not celeb
            s.push(i)

    if s.is_empty():
        print("No one is celebrity")
        return

    celeb = s.pop()

    # Final validation
    for i in range(len(l)):
        if i != celeb:
            if l[i][celeb] == 0 or l[celeb][i] == 1:
                print("No one is celebrity")
                return

    print("The celebrity is:", celeb)

find_the_celeb(l)
