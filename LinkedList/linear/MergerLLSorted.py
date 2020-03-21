class Node:
	def __init__(self, val = None):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	def mergeTwoLists(self, l1, l2):
		node1 = l1
		node2 = l2
		def Sort(node2):
			head = node2
			node = node2
			if node.next is not None:
				node1 = node.next
			else:
				return node2
			if node1 is not None:
				if node.val > node1.val:
					node.val, node1.val = node1.val, node.val
				else:
					
				node = node.next
				node1 = node1.next
			return head
			
		while node1 != None :
				
			if node1.val <= node2.val:
				
				if node1.next is None:
					node1.next = node2
					return l1
				node1 = node1.next
				
			elif node1.val > node2.val:
			
				node1.val, node2.val = node2.val, node1.val
				node2 = Sort(node2)
				if node1.next is None:
					node1.next = node2
					return l1
				node1 = node1.next
		
	def printlist(self):
		node = l1.head
		while node is not None:
			print(node.val, end = "->")
			node = node.next

l1 = LinkedList()
l1.head = Node(7)
e2 = Node(8)
e3 = Node(9)
l1.head.next = e2
e2.next = e3

l2 = LinkedList()
l2.head = Node(4)
f2 = Node(5)
f3 = Node(6)
l2.head.next = f2
f2.next = f3

l1.printlist()
l1.mergeTwoLists(l1.head, l2.head)
print()
l1.printlist()

	