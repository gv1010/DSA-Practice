import time

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
	
class Tree:
	def __init__(self, root):
		self.root =  Node(root)
		self.large = 0
		
	def size(self, root):
		if root is None:
			return 0
		return self.size(root.left) + self.size(root.right) + 1
	
	def isBST(self, root, lower = float('-inf'), higher = float('inf')):
		if root is None:
			return True
		if not lower < root.data < higher:
			return False
		return self.isBST(root.left, lower, root.data) and self.isBST(root.right, root.data, higher)
	
	def LargestBST(self, root):
		
		if root is None:
			return None
		self.LargestBST(root.left)
		self.LargestBST(root.right)
		if self.isBST(root, lower = float('-inf'), higher = float('inf')):
			curr_large = self.size(root)
			#print(curr_large)
			if curr_large >= self.large:
				self.large = curr_large
		
		#print('large', self.large)
		return self.large
    
tree = Tree(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(9)	
tree.root.right.right.right.left = Node(8)
start = time.time()
#print(tree.size(tree.root))
#print(tree.isBST(tree.root,lower = float('-inf'), higher = float('inf')))
print(tree.LargestBST(tree.root))
print(time.time()- start)