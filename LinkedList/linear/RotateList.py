class Node:
	def __init__(self, val= None):
		self.val = val
		self.next = None
class LL:
	def __init__(self, head):
		self.head = Node(head)
	def rotate(self, head, k):
		node = head
		count = 0
		while node:
			count = count+1
			node = node.next
		if k > count:
			k = k%count
		node = head
		tail = head
		for _ in range(k):
			tail = tail.next
		while tail.next:
			tail = tail.next
			node = node.next
		tail.next = head
		head = node.next
		node.next = None
		return head
	def printll(self, head):
		node = head
		while node:
			print(node.val, end = "->")
			node = node.next

	def odd_even(self, head):
		if head is None:
			return head
		if head.next is None:
			return head
		if head.next.next is None:
			return head
		odd_head = head
		even_head = head.next
		odd, even = odd_head, even_head
		while odd is not None and even is not None:
			print(odd.val, even.val)
			odd.next = even.next
			if even.next is None:
				break
			else:
				odd = even.next
				even.next = odd.next
				even = odd.next
		odd.next = even_head
		return head
		
l = LL(1)
l.head.next = Node(2)
l.head.next.next = Node(3)
#l.head.next.next.next = Node(4)
#l.head.next.next.next.next = Node(5)
#l.head.next.next.next.next.next = Node(6)
l.printll(l.head)
new = l.odd_even(l.head)
print()
l.printll(new)

			