class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		
class LinkedList:
	def __init__(self, head):
		self.head = Node(head)
		
	def mergeKlists(self, lists):
		import heapq
		arr = []
		count = 0
		for list in lists:
			count = count+1
			heapq.heappush(arr, (list.val, count, list))
		
		new_head = Node(float('inf'))
		temp = new_head
		while len(arr):
			_, _, node = heapq.heappop(arr)
			temp.next = node
			temp = node
			if node.next:
				count = count+1
				heapq.heappush(arr, (node.next.val, count,node.next))
		return new_head.next
		
	def printL(self, node):
		while node:
			print(node.val, end = "-")
			node = node.next
				
l1 = LinkedList(1)
l1.head.next = Node(3)
l1.head.next.next = Node(4)

l2 = LinkedList(3)
l2.head.next = Node(5)

node = l1.mergeKlists([l1.head, l2.head])
l1.printL(node)
			
			
		
			
		