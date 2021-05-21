class Stack:
        def _init_(self):
            self.items = []
            
        def isEmpty(self):
            return self.items == []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def peek(self):
            return self.items[len(self.items)-1]

        def size(self):
            return len(self.items)

        def min(self):
            return min(self.items)

        def movePeg(self, dest):
            if dest.isEmpty() == True:
                dest.push(self.pop())
            elif self.isEmpty() == True:
                self.push(dest.pop())
            else:
                if self.peek() > dest.peek():
                    self.push(dest.pop())
                else:
                    dest.push(self.pop())
                    
        def printPeg(self,myName):
            print(myName,self.items)

        def startPeg(self, disk):
            for i in range(disk,0,-1):
                self.push(i)


                
source = Stack()                    #Crarte source tower
temp = Stack()                      #Creare temporary tower
dest = Stack()                      #Create destination tower

disks = int(input("Enter the amount of disks: "))
source.startPeg(disks)
moves = (2**disks)                  #Calculate the amount of moves based on disks
print('< Start >')
source.printPeg('src')
temp.printPeg('tmp')
dest.printPeg('dst')
print('-----------------')


for i in range (moves-1):           #Loop through the amount of moves
    if disks%2 == 0:                #If the number of disks is even
        if i%3 == 0:                #Check if you are on the first move
            source.movePeg(temp)    #Leagal move from A to B
        elif i%3 == 1:              #Check if you are on the second move
            source.movePeg(dest)    #Legal move from A to C
        else:                       #Check if you are on the third mvoe
            temp.movePeg(dest)      #Legal move from B to C
    else:                           #If the number of disks are o
        if i%3 == 0:                #Check if you are on the first move
            source.movePeg(dest)    #Legal move from A to C
        elif i%3 == 1:              #Check if you are on the second move
            source.movePeg(temp)    #Legal move from A to B
        else:                       #Check if you are on the third move
            temp.movePeg(dest)      #Legal move from B to C
    print('< Move',i+1,'>') 

    source.printPeg('src')
    temp.printPeg('tmp')
    dest.printPeg('dst')

    print('-----------------')