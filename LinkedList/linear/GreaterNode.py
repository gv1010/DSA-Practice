class Node:
	def __init__(self,val = None):
		self.val = val
		self.next = None
class LL:
	def __init__(self,head):
		self.head = Node(head)
	def greaterNode(self, head):
		
		if head is None or head.next is None:
			return [0]

		q = []
		node = head
		count = 1
		while node.next:
			count = count + 1
			if node.val < node.next.val:
				q.append(node.next.val)
			node = node.next
		if len(q) == 0:
			return count*[0]
		
		node = head
		i = 0
		out = []
		while node :
			if node.val == q[i] and q[i+1] > q[i]:
				out.append(q[i+1])
				if i < len(q)-1:
					i = i+1
			elif node.val == q[i] and q[i] > q[i+1]:
				out.append(0)
				if i < len(q)-1:
					i = i+1
			elif i == len(q)-1 :
				if node.val < q[i]:
					out.append(q[i])
				else:
					out.append(0)
			elif node.val < q[i]:
				out.append(q[i])
			node = node.next
		return out
			
		
		
		
										#if head is None or head.next is None:
										#	return [head.val]
										#q = []
										#node = head
										#count = 1
										#while node.next:
										#	count = count + 1
										#	if node.val < node.next.val:
										#		q.append(node.next.val)
										#	node = node.next
		#node = head
		#i = 0
		#value = q[i]
		#out = []
		#while node:
		#	if node.next is None:
		#		out.append(0)
		#		
		#	if i < len(q)-1 and node.val == value and value > q[i+1]:
		#		out.append(0)
		#		i = i+1
		#		value = q[i]
		#		
		#	elif i < len(q)-1 and node.val == value and value < q[i+1]:
		#		i = i+1
		#		value = q[i]
		#		out.append(value)
		#		
		#	elif node.val < value:
		#		out.append(value)
		#		
		#	elif node.val == value:
		#		out.append(value)
		#		
		#	node = node.next
		#return out
					
		
	def print_ll(self, head):
		node = head
		while node:
			print(node.val , end = "->")
			node = node.next
		
2,7,4,3,5
1,7,5,1,9,2,5,1
ll = LL(1)
ll.head.next = Node(7)
ll.head.next.next = Node(5)
ll.head.next.next.next = Node(1)
ll.head.next.next.next.next = Node(9)
ll.head.next.next.next.next.next = Node(2)
ll.head.next.next.next.next.next.next = Node(5)
ll.head.next.next.next.next.next.next.next = Node(1)

ll.print_ll(ll.head)
print()
print(ll.greaterNode(ll.head))
#ll.print_ll(ll.head)

