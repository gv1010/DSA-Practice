class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        

    def push(self, x: int) -> None:
        self.items.append(x)
        
    def pop(self) -> None:
        if self.items != []:
            return self.items.pop()
        else:
            return None

    def top(self) -> int:
        if self.items != []:
            return self.items[-1]
        else: 
            return None


    def empty(self):
        return self.items == []
        
    def getMin(self) -> int:
        
        min = 999
        while not self.empty():
            temp = self.pop()
            top = self.top()
            if top < temp :
                min = top
                print(min)
            else:
                min = temp
                print(min)
        return min        

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
print(obj.getMin())