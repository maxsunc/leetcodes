class MinStack:

    def __init__(self):
        # a stack that lets you retrieve the min element at any time
        self.stack = []
        # everything must be O(1)
        self.minStack = []


    def push(self, value: int) -> None:
        # [4,2,5,7]
        # [4,2,2,2]
        self.stack.append(value)
        if not self.minStack:
            self.minStack.append(value)
        else:
            if self.minStack[-1] > value:
                self.minStack.append(value)
            else:
                self.minStack.append(self.minStack[-1])
        

        

    def pop(self) -> None:
        # pop from both stacks
        self.minStack.pop()
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()