class Node:
   def __init__(self , item):
        self.item = item 
        self.next = None


class Stack: 
      
    def __init__(self): 
        self.head = None


    def isempty(self): 
        if self.head == None: 
            return True
        else: 
            return False
      

    def push(self,data): 
          
        if self.head is None: 
            self.head=Node(data)              
        else: 
            newnode = Node(data) 
            newnode.next = self.head 
            self.head = newnode 


    def pop(self): 
        if self.isempty(): 
            return print('the stack is empty !')    
        else: 
            popnode = self.head 
            self.head = self.head.next
            popnode.next = None
            return popnode.item 


    def show(self):          
            iternode = self.head 
            if self.isempty(): 
                print("Stack Underflow")    
            else:     
                while(iternode != None):       
                    print(iternode.item,"->",end = " ") 
                    iternode = iternode.next
                return


stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()
stack.show()
print()
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.show()