class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]


stack = Stack()
stack.push(10)
stack.push(11)
stack.push(12)
stack.push(13)
stack.pop()
print(stack.peek())
