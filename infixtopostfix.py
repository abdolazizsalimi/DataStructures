class stack:
    def __init__(self):
        self.item = []
        self.size = 0
    
    
    def getSize(self):
        return len(self.item)
        
    
    def isEmpty(self):
        return self.item == []
        
    
    def peek(self):
        
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.item[0]
    
    
    def push(self, value):
        self.item.insert(0,value)
        print(self.item)
        
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.item.pop(0)
        return remove
 

def infixtopostfix(inex): 
    pr = {}
    pr["^"] = 4
    pr["*"] = 3
    pr["/"] = 3 
    pr["+"] = 2
    pr["-"] = 2 
    pr["("] = 1
    opstack = stack()
    postfix = []
    tokenlist = inex.split()
    print(tokenlist)  

    #read all of the element of your input
    for item in tokenlist : 
        if item.isalpha() or item in '123456789' :
            postfix.append(item)
        elif item == "(" :
            opstack.push(item)
        elif item == ")" : 
            toptoken = opstack.pop() 
            while toptoken!= "(":
                postfix.append(toptoken)
                toptoken = opstack.pop()
        else:
            while (not opstack.isEmpty()) and (pr[opstack.peek()] >= pr[item]):
                postfix.append(opstack.pop())
            opstack.push(item)    

    while not opstack.isEmpty():
        postfix.append(opstack.pop())
    return "".join(postfix)    


print(infixtopostfix(input("enter your phrase:  ").upper())) 