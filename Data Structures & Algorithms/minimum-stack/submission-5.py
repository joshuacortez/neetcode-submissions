class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None
        val = self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()
       
    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minstack:
            return None
        return self.minstack[-1]
