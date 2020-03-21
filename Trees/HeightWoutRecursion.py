class Node:
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None

class quueue:
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

	def height(self, root):
		
		q = []
		level  = 1
		q.append((root, level))
		left  = 0
		right = 0
		if root.left is None and root.right is None:
			return level
		while len(q):
			
			node, level = q.pop(0)
			if node.left:
				left = level + 1
				q.append((node.left, left))
			if node.right:
				right = level + 1
				q.append((node.right, right))
				
			if node.left is None and node.right is None:
				return level
				
		return max(left, right)
				

tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(8)
tree.root.left.right.right = Node(9)
#tree.root.right.left = Node(6)
#tree.root.right.right = Node(7)

print(tree.height(tree.root))
