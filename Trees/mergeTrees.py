class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def mergeTrees(self, root1, root2):
		
		if root1 is None and root2 is None:
			return None
			
		if root1 is None and root2 is not None:
			return root2
		if root1 is not None and root2 is None:
			return root1
		if root1 is not None and root2 is not None:
			root1.val = root1.val + root2.val
			
		root1.left = self.mergeTrees(root1.left, root2.left)
		root1.right = self.mergeTrees(root1.right, root2.right)
		
		return root1
		
	def treePrint(self, root):
		if root is None:
			return None
		self.treePrint(root.left)
		print(root.val, end = " ")
		self.treePrint(root.right)
t1 = Tree(1)
t1.root.left = Node(2)
t1.root.right = Node(3)

t2 = Tree(4)
t2.root.left = Node(5)
t2.root.right = Node(6)

t1.treePrint(t1.mergeTrees(t1.root, t2.root))