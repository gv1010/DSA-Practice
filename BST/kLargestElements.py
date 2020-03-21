import copy
class Node:
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		self.sum1 = 0
	def BST(self,root,k):
		if root is None:
			return None
	
	
	def revinOrder(self, root):
		
		#def inOrder(root):
		#	if root is None:
		#		return None
		#	
		#	if len(kElements)<k:
		#		inOrder(root.right)
		#		#print(kElements)
		#		if len(kElements) < k:
		#			kElements.append(root.data)
		#			inOrder(root.left)
		#kElements = []
		#inOrder(root)
		#return kElements
		
		def inorder(root ):
			if root is None:
				return None
			inorder(root.right)
			self.sum1 = self.sum1 + root.data
			root.data = self.sum1
			inorder(root.left)
			#return root
		
		inorder(root)
		#return list1
		def INorder(root):
			if root is None:
				return None
			INorder(root.left)
			print(root.data,end=" ")
			INorder(root.right)
		
		return INorder(root)
tree = Tree(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

(tree.revinOrder(tree.root))


