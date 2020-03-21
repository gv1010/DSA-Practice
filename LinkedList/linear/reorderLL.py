class Node:
	def __init__(self, val = None):
		self.val = val
		self.next = None
class LL:
	def __init__(self, head):
		self.head = Node(head)
		
	def Reorder(self, head):
		def middle_node(head):
			fast = head
			slow = head
			while fast and fast.next:
				fast = fast.next.next
				prev = slow
				slow = slow.next
			#print(slow.val)
			prev.next = None
			return slow
		middle = middle_node(head)
		print()
		self.printLL(middle)
		print()
		self.printLL(head)
		def reverse_list(head):
			prev = None
			curr = head
			while 1:
				if curr.next:
					front_head = curr.next
					curr.next = prev
					prev = curr
					curr = front_head
				else:
					curr.next = prev
					return curr
		rev_half = reverse_list(middle)
		print()
		self.printLL(rev_half)
		curr = head
		while 1:
			if curr.next is None:
				curr.next = rev_half
				break
			curr_next = curr.next
			if rev_half:
				rev_next = rev_half.next
				curr.next = rev_half
				rev_half.next = curr_next
				rev_half = rev_next
				curr = curr_next
			else:
				break
	def printLL(self, head):
		node = head
		while node:
			print(node.val, end = "->")
			node = node.next
	
ll = LL(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)
ll.head.next.next.next.next.next = Node(6)
ll.head.next.next.next.next.next.next = Node(7)


#ll.printLL(ll.head)
print(ll.Reorder(ll.head))
ll.printLL(ll.head)




				