class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_elements = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_elements) == 0 or x <= self.min_elements[-1]:
            # make sure there is not empty list error pops up.
            self.min_elements.append(x)

    def pop(self) -> None:
        current = self.stack.pop()

        if current == self.min_elements[-1]:
            # take out the last element in the min_elements list
            self.min_elements.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_elements[-1]

# Your MinStack object will be instantiated and called as such:
# x = 5
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()