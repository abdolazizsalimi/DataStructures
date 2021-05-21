class Node:
	def __init__(self, data):
		self.data = data 
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None



	def deleteNode(self, dele):
		

		if self.head is None or dele is None:
			return
		

		if self.head == dele:
			self.head = dele.next

		
			dele.next.prev = dele.prev
	

		if dele.prev is not None:
			dele.prev.next = dele.next
	



	def push(self, new_data):

		new_node = Node(new_data)
		new_node.next = self.head

		if self.head is not None:
			self.head.prev = new_node

		self.head = new_node


	def printList(self, node):
		while(node is not None):
			print(node.data)
			node = node.next


dll = DoublyLinkedList()


dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)

print("\n Original Linked List") 
dll.printList(dll.head)
dll.deleteNode(dll.head)
dll.deleteNode(dll.head.next)
dll.deleteNode(dll.head.next)

print ("\n Modified Linked List")
dll.printList(dll.head)
