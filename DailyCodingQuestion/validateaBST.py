class Node:
	def __init__(self, val):
		self.val = val
		self.left = next
		self.right = next
class Tree:
	def __init__(self, root):
		self.root = Node(root)
	def validateBST(self, root):
		if root is None:
			return None
		if root.left and root.right:
			if root.left.val < root.val < root.right.val:
				return True
			else:
				return False
		elif root.left and root.right is None:
			if root.val > root.left.val:
				return True
			else:
				return False
		elif root.left is None and root.rigth:
			if root.val < root.rigth.val:
				return True
			else:
				return Fasle
		return self.validate(root.left) and self.validateBST(root.right)
		
t = Tree(15)
t.root.left = Node(6)
t.root.right = Node(20)
t.root.left.left = Node(5)
t.root.left.right = Node(7)
t.root.right.left = Node(17)
t.root.right.right = Node(22)

print(t.validateBST(t.root))



		
			
			