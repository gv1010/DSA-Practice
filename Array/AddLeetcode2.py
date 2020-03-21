class Node:
	def __init__(self, val=None):
		self.val = val
		self.next = None
class LL:
	def __init__(self, head):
		self.head = Node(head)
		
	def addsum(self, head1, head2):
		if l1 is None:
			return l2
		if l2 is None:
			return l1
		node1 = head1
		node2 = head2
		carry = 0
		head3 = Node(0)
		node = head3
		while node1 or node2:
			adi = 0
			
			if node1:
				adi = adi + node1.val
				node1 = node1.next
			if node2:
				adi = adi + node2.val
				node2 = node2.next
			adi = carry + adi
			
			rem = adi%10
			carry = adi//10
			node.val = rem
			print(rem)
			prev = node
			node.next = Node(0)
			prev = node
			node = node.next
		if carry != 0:
			prev.next.val = carry
		if prev.next.val == 0:
			prev.next = None
		return head3
		
	def llprint(self, head):
		node = head
		while node:
			print(node.val, end = "-")
			node = node.next

ll = LL(2)
ll.head.next = Node(4)
ll.head.next.next = Node(3)

ll1 = LL(5)
ll1.head.next = Node(6)
ll1.head.next.next = Node(7)
#ll1.head.next.next.next = Node(9)

ll.llprint(ll.head)
new = ll.addsum(ll.head, ll1.head)
print()
ll.llprint(new)



			