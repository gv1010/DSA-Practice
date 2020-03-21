class Node:
	def __init__(self,data=None):
		self.data = data
		self.next = None
class CircularLinkedList:
	
	def __init__(self):
		self.head = None
	
	def insertAtBegin(self, data):
		
		new = Node(data)
		new.next = self.head
		temp = self.head
		if self.head is not None:
			while (temp.next != self.head):
				temp = temp.next
			temp.next = new
		else:
			new.next = new
			
		self.head = new
				
			
		#if temp is not None:
		#	while temp.next:
		#		temp = temp.next
		#	temp.next = self.head
		#else:
		#	temp.next = self.head
		
		
		
	def printList(self):
		temp = self.head
		sum = 0
		while (temp):
			sum = sum + temp.data
			print(temp.data)
			temp = temp.next
			if (temp == self.head):
				break
		print(sum)
			
			
cllist = CircularLinkedList()

cllist.insertAtBegin(4)
cllist.insertAtBegin(5)
cllist.insertAtBegin(6)
cllist.insertAtBegin(7)

cllist.printList()
		