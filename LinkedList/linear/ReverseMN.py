class Node:
	def __init__(self, val = None):
		self.val =  val
		self.next = None
class LinkedList:
	def __init__(self, head):
		self.head = Node(head)
		
	def reverse_mn(self, head, m, n):
		
		if head.next is None:
			return head
		node = head
		i = 1
		head_m = node
		head_b4m = None
	
		while i <= m-1:
			head_b4m = node
			node = node.next
			head_m = node
			i = i+1
		flag = False
		prev = None
		curr = head_m
		while i <= n:
			
			if curr is None:
				flag = True
				if head_b4m != None:
					head_b4m.next = prev
					head_m.next = curr
					self.print_ll(head)
					break

				else:
					head_m.next = curr
					head = prev
					self.print_ll(head)	
				
			else:
				front = curr.next
				curr.next = prev
				prev = curr
				curr = front
				i = i+1
				
		if flag == False:
			if head_b4m != None:
				head_b4m.next = prev
				head_m.next = curr
				self.print_ll(head)	

			else:
				head_m.next = curr
				head = prev
				self.print_ll(head)	
		
		
	def print_ll(self, head):
		node =  head
		while node:
			print(node.val, end = "->")
			node = node.next
			
	def remveDuplicates(self, head):
		node = head
		node1 = node
		node2 = node.next
		while node2:
			while node2 is not None and node1.val == node2.val:
				node2 = node2.next
			node1.next = node2
			node1 = node2
			if node2 is None:
				return head
			node2 = node2.next
		return head
	def partition(self, head, value ):
		node = head
		while node.next and node.next.val < value:
			node = node.next
		pivot = node
		ptr2 = pivot.next
		while ptr2 and ptr2.val >= value:
			ptr2 = ptr2.next
		pivot.next = ptr2.next
		pivot = pivot.next
			
			
			
LL = LinkedList(1)
LL.head.next = Node(1)
LL.head.next.next = Node(2)
LL.head.next.next.next = Node(2)
LL.head.next.next.next.next = Node(3)
LL.head.next.next.next.next.next = Node(4)
LL.head.next.next.next.next.next.next = Node(4)
print(LL.remveDuplicates(LL.head))
LL.print_ll(LL.head)
