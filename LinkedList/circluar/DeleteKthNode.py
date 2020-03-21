#Delete K th node froom the list
#deletc k th node from the list untill the list has only single element
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		
class CircularLL:
	def __init__(self):
		self.head = None
	def circular(self,data):
		new = Node(data)
		new.next = self.head
		temp = self.head
		if self.head is not None:
			while(temp.next != self.head):
				temp = temp.next
			temp.next = new
		else:
			new.next = new
		self.head = new
	
	def deleteKthNode(self,k):
		i = 1
		temp = self.head
		if k != 0:
			while i < k:
				i = i+1
				temp = temp.next
			if (temp.next == temp):
				return temp
			else:
				temp.next = temp.next.next
		else:
			return
	def deleteUntillSingleEle(self,k): 
		cll = CircularLL()
		temp = self.head
		while (temp.next != self.head):
			cll.deleteKthNode(k)
			cll.printList()
			temp = self.head

	
	def printList(self):
		temp = self.head
		while temp.next:
			print(temp.data)
			temp  = temp.next
			if (temp == self.head):
				break
		
cllist = CircularLL()
cllist.circular(1)
cllist.circular(2)
cllist.circular(3)
cllist.circular(4)
cllist.circular(5)


cllist.printList()
print("///////////////////////////////")
cllist.deleteKthNode(3)
cllist.printList()
print("///////////////////////////////")
cllist.deleteKthNode(3)
cllist.printList()
print("///////////////////////////////")
cllist.deleteKthNode(3)
cllist.printList()
#cllist.deleteUntillSingleEle(3)
#cllist.printList()
	
			
			
		
		
		
			