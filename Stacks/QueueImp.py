class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class queue:
	def __init__(self):
		self.head = None
		self.last = None
	
	def enqueue(self, data):
		if self.last == None:
			self.head = Node(data)
			self.last = self.head
		else:
			self.last.next = Node(data)
			self.last = self.last.next
	
	def dequeque(self):
		if self.head is None:
			return ('Queue empty')
		else:
			temp = self.head.data
			self.head = self.head.next
			return (temp)
			
	def print_q(self):
		val = self.head
		print('------------')
		while val:
			print(val.data)
			val = val.next


q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
#print(q.print_q())
print(q.dequeque())
print(q.dequeque())
print(q.dequeque())
#print(q.print_q())
print(q.print_q())
print(q.dequeque())
q.enqueue('aaa')
print(q.print_q())

	