class Node:	
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def MaxHeapify(self, root):
		if root is None:
			return None
			
		else:
			self.MaxHeapify(root.left)
			self.MaxHeapify(root.right)
			if root.left is None and root.right is None:
				return
			#max = Node(0)
			if root.left and root.right:
				if root.left.data > root.right.data:
					max = root.left
				else:
					max = root.right
					
			elif root.left and not root.right:
				if root.left.data > root.data:
					max = root.left
				else:
					return 
				
			if max.data > root.data:
				temp = max.data
				max.data = root.data
				root.data = temp
				self.MaxHeapify(max)
				
	def inorder(self, root):
		if root is None:
			return
		self.inorder(root.left)
		print(root.data, end = " ")
		self.inorder(root.right)
		
tree = Tree(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

tree.inorder(tree.root)
print()
tree.MaxHeapify(tree.root)
#tree.heapify(tree.root)
print()
tree.inorder(tree.root)
