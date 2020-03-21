class stack:
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def is_empty(self):
		return len(self.items) == 0
		
class queue:
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.append(item)
	def dequeue(self):
		return self.items.pop(0)
	def is_empty(self):
		return len(self.items) == 0
		
class Node:
	def __init__(self, value =None):
		self.value = value
		self.left = None
		self.right = None

class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def reverselevel(self, root):
		if root is None:
			return
		q = queue()
		s = stack()
		q.enqueue(root)
		traversal = "-"
		while not q.is_empty():
			node = q.dequeue()
			s.push(node)
			if node.right:
				q.enqueue(node.right)
			if node.left:
				q.enqueue(node.left)
			
		while not s.is_empty():
			node = s.pop()
			traversal += str(node.value)+ "-"
			
		return traversal
			
tree =  Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.reverselevel(tree.root))
		
	