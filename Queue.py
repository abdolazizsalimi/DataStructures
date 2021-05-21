class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []



    def addQ(self,x):
        self.stack1.append(x)


    def popQueue(self): 
    
            if len(self.stack1) == 0 and len(self.stack2) == 0: 
                print("Q is Empty") 
                return
            elif len(self.stack2) == 0 and len(self.stack1) > 0: 
                while len(self.stack1): 
                    self.stack2.append(self.stack1.pop()) 
                return self.stack2.pop() 
            else: 
                return self.stack2.pop() 




q = Queue()
q.addQ(1)
q.addQ(2)
q.addQ(4)
q.addQ(4)
q.addQ(4)
q.addQ(4)
q.addQ(4)
print(q.popQueue())
print(q.popQueue())
print(q.popQueue())
print(q.popQueue())
print(q.popQueue())
print(q.popQueue())
q.addQ(3)
