class Node:
	def __init__(self,data = None):
		self.data = data
		self.next = None
class LinkedList:
	def __inti__(self):
		self.head = None
		
	def InsertAtEnd(self,data):
		new_node = Node(data)
		temp = self.head
		while temp.next:
			temp = temp.next
		temp.next = new_node
			
		
	def listPrint(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
			
	def DeleteDuplicate(self):
		temp = self.head
		empt = []
		if temp.next is None:
			return temp
		while temp:
			
			if (temp.data in empt):
				temp = temp.next
				prev.next = temp
			else:
				empt.append(temp.data)
				prev = temp
				temp = temp.next
	
			
llist = LinkedList()
llist.head = Node("Mon")
llist.InsertAtEnd("Mon")
llist.InsertAtEnd("Tue")

#l2 = Node("Tue")
#l3 = Node("Tue")
#llist.head.next = l1
#l1.next = l2
#l2.next = l3

#llist.listPrint()
llist.DeleteDuplicate()

llist.listPrint()
			
			