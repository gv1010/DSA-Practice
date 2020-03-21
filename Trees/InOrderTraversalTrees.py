class Node:
	def __init__(self,value=None):
		self.value = value
		self.left = None
		self.right = None
		
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def inorder_traversal(self, root, traversal):
		if root:
			traversal = self.inorder_traversal(root.left, traversal)
			traversal += str(root.value) + "-"
			traversal = self.inorder_traversal(root.right, traversal)
		return traversal
		
	def print_tree(self):
		print(self.inorder_traversal(self.root, ''))
		return True
		
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree())
