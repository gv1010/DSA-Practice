class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	
class queue:
	def __init__(self):
		self.items = []
	def enqueue(self, data):
		self.items.append(data)
	def dequeue(self):
		return self.items.pop(0)
	def isempty(self):
		return len(self.items) == 0
		
		
class Tree:
	def __init__(self, root):
		self.root = Node(root)
	
	def size(self, root):
		q = queue()
		size = 0
		if root:
			q.enqueue(root)
			size = 1
		
		while not q.isempty():
			node = q.dequeue()
			if node.left:
				q.enqueue(node.left)
				size = size + 1
			if node.right:
				q.enqueue(node.right)
				size = size + 1
		return size
		
		
tree =  Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.size(tree.root))