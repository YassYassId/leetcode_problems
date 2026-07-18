class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minimum = 0
        

    def push(self, val: int) -> None:
        if len(self.minStack) == 0 or self.minStack[-1] >= val:
            self.minStack.append(val)
            self.minimum = val 
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            temp = self.stack.pop()
            if self.minStack and self.minStack[-1] == temp:
                self.minStack.pop()
        if self.minStack:
            self.minimum = self.minStack[-1]

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minimum
        else:
            return None
        
