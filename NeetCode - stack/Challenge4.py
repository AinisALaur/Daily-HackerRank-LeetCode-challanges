class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if(len(self.s2) == 0):
            for i in range(len(self.s1)):
                self.s2.append(self.s1[-1])
                self.s1.pop()
        
        return self.s2.pop()

    def peek(self) -> int:
        if(len(self.s2) != 0):
            return self.s2[-1]
        else:
            return self.s1[0]

    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0

queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)

print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())

print(queue.empty())