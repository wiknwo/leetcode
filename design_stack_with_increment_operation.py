class CustomStack:

    def __init__(self, maxSize: int):
        self.mystack = []
        self.maxsize = maxSize
        

    def push(self, x: int) -> None:
        if len(self.mystack) != self.maxsize:
            self.mystack.append(x)
        

    def pop(self) -> int:
        if not self.mystack:
            return -1
        return self.mystack.pop()

    def increment(self, k: int, val: int) -> None:
        if len(self.mystack) < k:
            newstack = []
            while self.mystack:
                newstack.append(self.mystack.pop() + val)
            while newstack:
                self.mystack.append(newstack.pop())
        else:
            newstack, count = [], 0
            while self.mystack:
                newstack.append(self.mystack.pop())
            while newstack:
                value = newstack.pop()
                if count < k:
                    value += val
                count += 1
                self.mystack.append(value)
            
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)