class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
class LinkedList:
	def __init__(self, head):
		self.head = Node(head)
	def addSum(self, head1, head2):
		if head1.next is None and head2.next is None:
			add = head1.val + head2.val
			rem = add%10
			carry = add//10
			node = Node(rem)
			return node, carry
		node, carry = self.addSum(head1.next, head2.next)
		add = head1.val + head2.val + carry
		rem = add%10
		carry = add//10
		curr_node = Node(rem)
		curr_node.next = node
		return curr_node, carry
	def addSumUtil(self, head1, head2):
		def func(head1, head2, counter):
			if counter == 0:
				node, carry = self.addSum(head1, head2)
				return node, carry
			counter = counter - 1
			node, carry = func(head1.next, head2, counter)
			add = head1.val + carry
			rem = add%10
			carry = add//10
			curr_node = Node(rem)
			curr_node.next = node
			return curr_node, carry
			
		node1, node2 = head1, head2
		count1, count2 = 0, 0
		while node1:
			count1 = count1 + 1
			node1 = node1.next
		while node2:
			count2 = count2 + 1
			node2 = node2.next
		if count1 > count2:
			node, carry = func(head1, head2,count1-count2)
		elif count2 > count1:
			node, carry = func(head2, head1, count2-count1)
		else:
			node, carry = self.addSum(head1, head2)
		if carry == 0:
			return node
		else:
			curr_node = Node(carry)
			curr_node.next = node
			return curr_node
	def printLL(self,head):
		while head:
			print(head.val, end = "-")
			head = head.next
			
L1 = LinkedList(9)
L1.head.next = Node(2)
L1.head.next.next = Node(3)

L2 = LinkedList(9)
#L2.head.next = Node(2)
#L2.head.next.next = Node(1)


L1.printLL(L1.head)
print()
L1.printLL(L2.head)
print()
print('-'*60)
node = L1.addSumUtil(L1.head, L2.head)
L1.printLL(node)

			
		