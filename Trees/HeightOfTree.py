class Node:
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

class Tree:
	def __init__(self, root):
		self.root = Node(root)
	def height(self, root):
		if root is None:
			return -1
		left = self.height(root.left)
		right = self.height(root.right)
		
		return 1 + max(left, right)
		
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.left.left = Node(6)
tree.root.left.right.right = Node(7)

print(tree.height(tree.root))
