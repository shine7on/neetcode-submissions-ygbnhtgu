class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(self.stack)

    def pop(self) -> None:
        print('pop')
        self.stack.pop()

    def top(self) -> int:
        print(self.stack)
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        
