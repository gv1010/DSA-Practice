class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def stringPreorder(self, root, s = "" ):
		if root is None:
			return 
		s = s + str(root.val)
		if root.left and root.right is None:
			s = s + '[' + str(self.stringPreorder(root.left))  + ']'
		elif root.left:
			s = s + '[[' + str(self.stringPreorder(root.left))  + ']'
		else:
			self.stringPreorder(root.left)
		if root.right and root.left is None:
			s = s + '[' + str(self.stringPreorder(root.right))  + ']'
		elif root.right:
			s = s + '[' + str(self.stringPreorder(root.right))  + ']]'
		else:
			self.stringPreorder(root.right)
		return s 
		
t = Tree(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
#t.root.left.right = Node(5)
#t.root.right.left = Node(6)
#t.root.right.right = Node(7)

print(t.stringPreorder(t.root))