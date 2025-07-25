

class stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1
    def push(self,value):
        if self.top == self.size -1:
            return "overflow"
        else:
            self.top +=1
            self.stack[self.top]= value

    def pop(self):
        if self.top == -1:
            return "underflow"
        else:
            data = self.stack[self.top]
            self.top -=1
            return data

    def traverse(self):
        for i in range(self.top +1 ):
            print(self.stack[i],end=' ')

s = stack(3)
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.pop())
print(s.pop())
print(s.traverse())
