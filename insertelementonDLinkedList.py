
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class LinkedList:
  def __init__(self):
    self.head = None


  def push(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode
      newNode.prev = temp


  def push_at(self, newElement, position):     
    newNode = Node(newElement)
    if(position < 1):
      print("\nposition should be >= 1.")
    elif (position == 1):
      newNode.next = self.head
      self.head.prev = newNode
      self.head = newNode
    else:
      temp = self.head
      for _ in range(1, position-1):
        if(temp != None):
          temp = temp.next   
      if(temp != None):
        newNode.next = temp.next
        newNode.prev = temp
        temp.next = newNode  
        if (newNode.next != None):
          newNode.next.prev = newNode
      else:
        print("\nThe previous node is null.")  


  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("\nThe list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
    else:
      print("\nThe list is empty.")
MyList = LinkedList()


MyList.push(10)
MyList.push(20)
MyList.push(30)
MyList.PrintList()


MyList.push_at(100, 2)
MyList.PrintList() 


MyList.push_at(200, 1)
MyList.PrintList() 