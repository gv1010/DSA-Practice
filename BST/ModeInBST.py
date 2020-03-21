class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def dump(self, root):	
		def findMode(root):
			if root.left is None and root.right is None:
				return
			if (root.left and root.data == root.left.data) or (root.right and root.data == root.right.data):
				if root.data not in mode:
					mode.append(root.data)
			findMode(root.left)
			findMode(root.right)
		mode = []
		findMode(root)
		return mode

tree = Tree(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(2)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(6)
#tree.root.right.right.right = Node(9)	
#tree.root.right.right.right.left = Node(8)

print(tree.dump(tree.root))