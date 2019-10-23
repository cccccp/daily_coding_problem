class stack_with_max: #We additionally store the list of the current maximums to obtain O(1) time complexity for the operations
    def __init__(self):
        self.list=[]
        self.currentmaxs=[]
    def pop(self):
        self.list.pop()
        self.currentmaxs.pop()
    def Max(self):
        if len(self.list)>0:
            return self.currentmaxs[-1]
        else:
            return None
    def push(self,x):
        if len(self.list)>0:
            self.currentmaxs.append(max(x,self.currentmaxs[-1]))
        else:
            self.currentmaxs.append(x)
        
        self.list.append(x)
