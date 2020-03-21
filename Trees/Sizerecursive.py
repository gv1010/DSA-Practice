class Node:
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def size_recursive(self, node):
		if node is None:
			return 0
		return 1 + size_recursive(node.left) + size_recursive(node.right)
		
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.right = Node(4)
tree.root.left.left = Node(5)
tree.root.left.left.left = Node(6)
tree.root.left.left.right= Node(7)

print(tree.size_recursive(tree.root))
		