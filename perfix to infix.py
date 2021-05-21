
class Calculator:
    def __init__ (self):
        self.stack = []

    def push (self, p):
        if p in ['+', '-', '*', '/']:
            op1 = self.stack.pop ()
            op2 = self.stack.pop ()
            if p== '-':
                self.stack.append (op1 - op2 )
            elif p == '+':
                self.stack.append (op1 + op2 )             
            elif p == '*':
                self.stack.append (op1 * op2 )    
            elif p == '/':
                self.stack.append (op1 / op2 )
        else:
            self.stack.append (p)

    def change (self, l): 
        l.reverse ()
        for i in l:
            self.push (i)
        return self.stack.pop ()

c = Calculator ()

print (c.change ( ['+','*', 8, 9 ,10] ))
