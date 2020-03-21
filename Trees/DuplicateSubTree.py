class Node:
	def __init__(self, val = None):
		self.val = val
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		self.save = ""
	def duplicate(self, root, flag):
		if root is None:
			if flag:
				return 'lnull'
			else:
				return 'rnull'

		str1 = "#" + str(root.val)+str(self.duplicate(root.left, True)) + str(self.duplicate(root.right, False))
		return str1
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(2)
tree.root.right.left.left = Node(4)
tree.root.right.right = Node(5)

print(tree.duplicate(tree.root, True)) 

#print(tree.save)
		
