class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
        else:
            self.stack += [val]

    def pop(self) -> None:
        self.stack = self.stack[:- 1]

    def top(self) -> int:
        if not self.stack:
            return 0
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        currMin = float('inf')
        if self.stack:
            for val in self.stack:
                if currMin > val:
                    currMin = val
            return currMin
        else:
            return 0
