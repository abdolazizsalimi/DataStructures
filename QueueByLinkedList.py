
class Node: 
	
	def __init__(self, data): 
		self.data = data 
		self.next = None


class Queue: 
	
	def __init__(self): 
		self.front = self.rear = None

	def isEmpty(self): 
		return self.front == None
	

	def addelement(self, item): 
		temp = Node(item) 
		if self.rear == None: 
			self.front = self.rear = temp 
			return
		self.rear.next = temp 
		self.rear = temp 


	def deletelement(self): 	
		if self.isEmpty(): 
			return
		temp = self.front 
		self.front = temp.next
		if(self.front == None): 
			self.rear = None


q = Queue() 
q.addelement(10) 
q.addelement(20) 
q.addelement(30) 
q.addelement(40) 
q.addelement(50) 
q.deletelement()  
q.deletelement() 

print("Queue Front:" + str(q.front.data)) 
print("Queue Rear:" + str(q.rear.data)) 

