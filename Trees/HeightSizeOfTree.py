class Node:
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None
class Stack:
	def __init__(self):
		self.items = []
		
	def push(self, data):
		return self.items.append(data)
		
	def pop(self):
		if self.is_empty() is not None:
			return self.items.pop()
			
	def is_empty(self):
		return self.items == []
		
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def height(self, root):
		if root is None:
			return -1
		left = self.height(root.left)
		right = self.height(root.right)
		return 1 + max(left, right)
		
	def size(self):
		if self.root is None:
			return None
		s = Stack()
		s.push(self.root)
		size = 1
		while not s.is_empty():
			node = s.pop()
			if (node.left):
				s.push(node.left)
				size = size + 1
			if (node.right):
				s.push(node.right)
				size = size + 1
		return size
				
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.left.left = Node(6)
tree.root.left.right.right = Node(7)

print(tree.size())
