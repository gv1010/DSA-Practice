class Node:
    def __init__(self,data=None):
        self.dataval = data
        self.nextval = None

class LinkedList:

	def __init__(self):
		self.headval = None
		
	def reverse_mn(self, head):
	
		
	def reverse__(self):
		curr = self.headval
		prev = None
		while 1:
			if curr.nextval != None:
				front = curr.nextval
				curr.nextval = prev
				prev = curr
				curr = front
			else:
				curr.nextval = prev
				self.headval = curr
				break
				#return self.headval
		return 1
	def insertnode(self):
		print('No of elements to be added')
		inp = int(input())
		list2 = LinkedList()
		x = list2.headval
		for i in range(inp):
			val = (input())
			x = Node(val)
			x = x.nextval

	def printlist(self):
		printval = self.headval
		#print(printval)
		while printval is not None:
			print(printval.dataval, end = "->")
			printval = printval.nextval
        
list1 = LinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thur")

#list1.headval.nextval = e2
#e2.nextval = e3
#e3.nextval = e4


list1.printlist()
list1.reverse__()
print()
list1.printlist()  
    