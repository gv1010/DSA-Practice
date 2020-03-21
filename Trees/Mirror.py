import copy
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
	
	def Mirror(self, root):
		if root is None:
			return None
		node = copy.deepcopy(root)
		#left = 
		#right = 
		node.left = self.Mirror(root.right)
		node.right = self.Mirror(root.left)
		return node
		
	def inorder(self, root, list_= ""):
		if root:
			list_ = self.inorder(root.left, list_)
			list_ = list_ + str(root.data) + " "
			list_ = self.inorder(root.right, list_)
		return list_
		
		
		
		
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.inorder(tree.root, ""))
print()
print(tree.inorder(tree.Mirror(tree.root), ""))
