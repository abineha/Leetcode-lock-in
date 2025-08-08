class FreqStack:

    def __init__(self):
        self.stack, self.count = {}, {}
        self.max_count = 0

    def push(self, val: int) -> None:
        val_count = self.count.get(val, 0) + 1
        self.count[val] = val_count

        if val_count > self.max_count:
            self.max_count = val_count
            self.stack[self.max_count] = []
        
        self.stack[val_count].append(val)

    def pop(self) -> int:
        result = self.stack[self.max_count].pop()
        self.count[result] -= 1
        
        if not self.stack[self.max_count]:
            self.max_count -= 1
        
        return  result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()