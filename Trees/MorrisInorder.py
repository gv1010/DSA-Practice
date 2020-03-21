class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
class Tree:
	def __init__(self, root):
		self.root = Node(root)
	def morris(self, root):
		current = root
		while current is not None:
			if current.left is None:
				print(current.data, "-")
				current = current.right
			else:
				pred = current.left
				while pred.right is not None:
					pred = pred.right
				if pred.right is None:
					pred.right = current
					current = current.left
					
					
					