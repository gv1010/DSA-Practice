class Node:
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right =  None
		
		
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def Successor(self, root, key):
		if root is None: 
			return None
		node = root
		large = 0
		while node:
			if node.data > key:
				large = node.data
				node = node.left
			else:
				node = node.right
		return large
	def Precessor(self, root, key):
		if root is None: 
			return None
		node = root
		small = 0
		while node:
			if node.data >= key:
				
				node = node.left
			else:
				small = node.data
				node = node.right
		return small
				
	def BST(self, root):
		if root is None:
			return None
		node = root
		s = []
		while 1:
			while node:
				s.append(node)
				node = node.left

			if len(s) == 0:
				break
			node = s.pop()
				
			if node and node.right is None:
				key = node.data
				#print(key)
				successor = self.Successor(root, key)
				pressor = self.Precessor(root, key)
				print('key',key)
				print('successor', successor)
				if successor-key == 1 or pressor - key:
					return True
				
			#print(node.data, end=" ")
			node = node.right
		return False
tree = Tree(47)
#tree.root.left = Node(7)
tree.root.right = Node(58)
#tree.root.left.left = Node(2)
#tree.root.left.right = Node(18)
#tree.root.right.left = Node(9)
tree.root.right.right = Node(116)
#tree.root.right.right.right = Node(43)
tree.root.right.right.left = Node(114)
#tree.root.right.right.right = Node(9)	
#tree.root.right.right.right.left = Node(8)

print(tree.BST(tree.root))				