class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	def push(self,data):
		new = Node(data)
		temp = self.head
		new.next = self.head
		if self.head is not None:
			while (temp.next != self.head):
				temp = temp.next
			temp.next = new
		else:
			new.next = new
		self.head = new
		
	def deleteEveryKth(self,k):
		temp = self.head
		while (self.head != self.head.next):
			for i in range(k-1):
				temp = temp.next
			self.head = temp.next
			temp.next = temp.next.next
		return self.head
		
			
	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
			if (temp == self.head):
				break
			
llist = LinkedList()
#llist.push(9)
#llist.push(8)
#llist.push(7)
#llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)		


llist.printList()
llist.deleteEveryKth(4)	
print('////////////////////////')
llist.printList()	