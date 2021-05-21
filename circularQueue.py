class CircularQueue(): 


	def __init__(self, size):
		self.size = size 
		self.queue = [None for i in range(size)] 
		self.front = self.rear = -1

	def addelement(self, data): 

		if ((self.rear + 1) % self.size == self.front): 
			print(" Queue is Full\n") 
			

		elif (self.front == -1): 
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data 
		else: 

			self.rear = (self.rear + 1) % self.size 
			self.queue[self.rear] = data 
			
	def deletelement(self): 
		if (self.front == -1):  
			print ("Queue is Empty\n") 
			

		elif (self.front == self.rear): 
			temp=self.queue[self.front] 
			self.front = -1
			self.rear = -1
			return temp 
		else: 
			temp = self.queue[self.front] 
			self.front = (self.front + 1) % self.size 
			return temp 

	def show(self): 
	

		if(self.front == -1): 
			print ("Queue is Empty") 

		elif (self.rear >= self.front): 
			print("Elements in the circular queue are:", 
											end = " ") 
			for i in range(self.front, self.rear + 1): 
				print(self.queue[i], end = " ") 
			print () 

		else: 
			print ("Elements in Circular Queue are:", 
										end = " ") 
			for i in range(self.front, self.size): 
				print(self.queue[i], end = " ") 
			for i in range(0, self.rear + 1): 
				print(self.queue[i], end = " ") 
			print () 

		if ((self.rear + 1) % self.size == self.front): 
			print("Queue is Full") 


ob = CircularQueue(5) 
ob.addelement(14) 
ob.addelement(22) 
ob.addelement(13) 
ob.addelement(-6) 
ob.show() 
print ("Deleted value = ", ob.deletelement()) 
print ("Deleted value = ", ob.deletelement()) 
ob.show() 
ob.addelement(9) 
ob.addelement(20) 
ob.addelement(5) 
ob.show() 


