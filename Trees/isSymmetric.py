class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def isSymmetry(self, root):
		root1 = root.left
		root2 = root.right
		def check(root1, root2):
			if root1 == None and root2 == None:
				return True
			elif root1 and root2:	
				return root1.data == root2.data and check(root1.left, root2.right) and check(root1.right, root2.left)
			return False
		return check(root1, root2)
		
	def univalue(self, root):
		if root is None:
			return 0
		left = 0
		right = 0
		
		if root.left  and root.left.data == root.data:
			left = 1 + self.univalue(root.left)
		
		if root.right and root.right.data == root.data:
			right = 1 + self.univalue(root.right)
		
		return left + right
		
tree = Tree(2)
tree.root.left = Node(1)
tree.root.right = Node(1)
tree.root.left.left = Node(1)
#tree.root.left.left.left = Node(1)
#tree.root.left.right = Node(3)
#tree.root.right.left = Node(4)
tree.root.right.right = Node(1)

print(tree.univalue(tree.root))
#print(tree.isSymmetry(tree.root))