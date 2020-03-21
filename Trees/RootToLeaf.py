class Node:
	def __init__(self, val=None):
		self.val = val
		self.left = None
		self.right = None
	
class Tree:
	def __init__(self,root):
		self.root = Node(root)
		self.min_sum = float('inf')
	def inorder(self, root, sum = 0):
		if root.left is None and root.right is None:
			self.min_sum = min(self.min_sum, sum+root.val)
			return None
		if root.left:
			self.inorder(root.left, sum+root.val)
		if root.right:
			self.inorder(root.right, sum+root.val)
			
			
			
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(-5)
tree.root.right.left = Node(-6)
#tree.root.right.right = Node(7)

tree.inorder(tree.root)
print(tree.min_sum)