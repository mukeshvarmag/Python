class MinStack:
    min=float('inf')
    def __init__(self):
        self.min=float('inf')
        self.stack = []
    
    def push(self, x):
        if x< self.min:
            self.min = x
        self.stack.append(x)
        


    # @return nothing
    def pop(self):
        if len(self.stack)>0:
            
            t=self.stack.pop()
            if t == self.min:
                if len(self.stack)>0:
                    self.min = min(self.stack)
                else:
                    self.min =float('inf')
        
            

    # @return an integer
    def top(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return -1


    # @return an integer
    def getMin(self):
        if len(self.stack)>0:
            return self.min
        else:
            return -1
        
        


