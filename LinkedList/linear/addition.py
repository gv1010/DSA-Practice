class Node:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next
class LinkedList:
	def __init__(self, head):
		self.head = Node(head)
	def add(self,node0, node1, carry):
		if not node0 and not node1 and not carry:
			return None

		node0_val = node0.val if node0 else 0
		node1_val = node1.val if node1 else 0
		total = node0_val + node1_val + carry

		node0_next = node0.next if node0 else None
		node1_next = node1.next if node1 else None
		carry_next = 1 if total >= 10 else 0

		return Node(total % 10, self.add(node0_next, node1_next, carry_next))
		
	def printl(self, node):
		if node is None:
			return None
		print(node.val, end = "-")
		node = node.next
l = LinkedList(1)	
l.head.next = Node(1)
l.head.next.next = Node(1)

#l.next.next = Node(4)

l1 = LinkedList(1)
l1.head.next = Node(3)
l1.head.next.next = Node(3)

node = l.add(l.head, l1.head, 0)
print(l.printl(node))

