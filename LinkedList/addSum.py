class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
class Linkedlist:
	def __init__(self, head):
		self.head = Node(head)
	def addNum(self, node1, node2):
		if node1.next is None and node2.next is None:
			value = node1.val + node2.val
			carry = value//10
			value = value%10
			node = Node(value)
			return node, carry
		node, carry = self.addNum(node1.next, node2.next)
		value = node1.val + node2.val + carry
		carry = value//10
		value = value%10
		curr_node = Node(value)
		curr_node.next = node
		return curr_node, carry
		
	def recurse(self, head, carry):
		if head.next == node1:
			value = head.val + carry
			carry = value//10
			value = value%10
			node = Node(value)
			return node, carry
		node, carry = self.recurse(head.next)
		value = head.val + carry
		carry = value//10
		value = value%10
		curr_node = Node(value)
		curr_node.next = node
		return curr_node, carry
		
	def operations(self, head1, head2):
		count1 = 0
		count2 = 0
		node1 = head1
		node2 = head2
		while node1:
			node1 = node1.next
			count1 = count1+1
		while node2:
			node2 = node2.next
			count2 = count2+1
		if count1 > count2:
			node1 = head1
			for _ in range(count1-count2):
				node1 = node1.next
			node, carry = self.addNum(node1, node2)
			if carry > 0:
				curr_node, carry = self.recurse(head1, carry)
				curr_node = Node()
				
		elif count1 < count2:
			node2 = head2
			for _ in range(count2-count1):
				node2 = node2.next
			node, carry = self.addNum(node1, node2)
			if carry > 0:
				curr_node, carry = self.recurse(head2, carry)
		else:
			carry = 0
			node, carry = self.addNum(node1, node2)
			if carry > 0:
				curr_node = Node(carry)
				curr_node.next = node
			
		
	def printNode(self, head):
		while head:
			print(head.val, end = "-")
			head = head.next
		
L1 = Linkedlist(9)
L1.head.next = Node(2)
L1.head.next.next = Node(3)

L2 = Linkedlist(2)
L2.head.next = Node(3)
L2.head.next.next = Node(4)

node, carry = L1.addNum(L1.head, L2.head)
L1.printNode(node)
print(>-----carry)



			
	