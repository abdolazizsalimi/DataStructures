class Stack:
    def __init__(self):
        self.a = []
    def isEmpty(self):
        return self.a == []
    def push(self,i):
        self.a.append(i)
    def pop(self):
        return self.a.pop()
    def peek(self):
        return self.a[len(self.a)-1]

def infixToPrefix(s):
    prec = {'/':3,'*':3,'+':2,'-':2,'^':4,'(':1}
    opStack = Stack()

    prefixList = []
    temp = []
    for token in s:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                temp.append(topToken)
                topToken = opStack.pop()
                print(temp)
            prefixList = temp + prefixList
            temp = []
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()]>= prec[token]):
                temp.append(opStack.pop())
            prefixList = temp + prefixList
            temp = []
            opStack.push(token)
    while not opStack.isEmpty():
        temp.append(opStack.pop())
    prefixList = temp + prefixList
    return ''.join(prefixList)
print (infixToPrefix("(A+B)*C-(D-E)*(F+G)"))