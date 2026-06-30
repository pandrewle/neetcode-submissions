class MinStack:

    def __init__(self):
        self.minVal = float('inf')
        self.mins = []
        self.tops = []
        self.stack = []

    def push(self, val: int) -> None:
        if val <= self.minVal:
            self.minVal = val
            self.mins.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()

        if self.mins and val == self.mins[-1]:
            self.mins.pop()
            self.minVal = self.mins[-1] if self.mins else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print(self.mins)
        return self.mins[-1]
