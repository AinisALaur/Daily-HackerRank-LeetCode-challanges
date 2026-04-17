class FreqStack:
    def __init__(self):
        self.freq = {}
        self.groups = {}
        self.max = -1

    def print(self):
        for key, val in self.groups.items():
            print(key, val)

    def push(self, val: int) -> None:
        self.freq[val] = 1 + self.freq.get(val, 0)

        if self.freq[val] > self.max:
            self.max = self.freq[val]
        
        if self.freq[val] not in self.groups:
            self.groups[self.freq[val]] = [val]
        else:
            self.groups[self.freq[val]].append(val)

    def pop(self) -> int:
        if len(self.groups[self.max]) == 0:
            self.max -= 1
        
        val = self.groups[self.max].pop()
        self.freq[val] -= 1

        return val
    

stack = FreqStack()
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(2)

print(stack.pop())
print(stack.pop())

stack.print()

stack.push(2)
stack.push(2)
stack.push(1)

print(stack.pop())
print(stack.pop())
print(stack.pop())
