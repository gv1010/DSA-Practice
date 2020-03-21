class Node:
	def __init__(self,data = None):
		self.data = data
		self.left = None
		self.right = None
		
class BT:
	def __init__(self, root):
		self.root = Node(root)
	
	def height(self, root):
		if root is not None:
			left_h = self.height(root.left)
			right_h = self.height(root.right)
			return 1 + max(left_h, right_h)
		else:
			return -1
	
	def diameter(self, root):
		if root is None:
			return 0
		left_sub = 0
		right_sub = 0
		if root.left:
			left_sub = self.height(root.left)
		if root.right:
			right_sub = self.height(root.right)
			
		print('left_sub', left_sub)
		print('right_sub', right_sub)
		return 1 + left_sub+1 + right_sub+1
		
		
tree = BT(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right =Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.diameter(tree.root))