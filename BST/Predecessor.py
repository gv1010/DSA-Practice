class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def Successor(self, root, key):
		node = root
		large = None
		small = None
		while node:
			
			if node.data >= key:
				node = node.left
			
			else:
				small = node.data
				node = node.right
		node = root
		while node:
			
			if node.data > key:
				large = node.data
				node = node.left
			
			else:
				#small = node.data
				node = node.right
		return small, large
		
	def getCountOfNode(self,root,l,h):
		self.count = 0
		def inorder(root,l,h):
			if root is None:
				return None
			inorder(root.left,l,h)
			if l<= root.data <= h:
				self.count = self.count + 1
			inorder(root.right,l,h)   
		
		inorder(root,l,h)
		return self.count
tree = Tree(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(9)	
tree.root.right.right.right.left = Node(8)

print(tree.getCountOfNode(tree.root, 1, 6))
		