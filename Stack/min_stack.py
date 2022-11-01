class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_value = min(val if not self.min_stack else self.min_stack[-1], val)
        if self.min_stack[-1] != min_value:
            self.min_stack.append(min_value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.push(1)
obj.push(5)
obj.push(4)
obj.push(3)
obj.push(2)
obj.push(8)
obj.push(5)
print(obj.min_stack)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
