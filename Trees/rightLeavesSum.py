class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
	def  right(self, root, flag, rlSum):
		if flag == True and root.left is None and root.right is None:
			rlSum[0] = rlSum[0] + root.val
			return None
		elif root is None:
			return None
		if root.left :
			flag = False
			self.right(root.left, flag, rlSum)
		if root.right:
			flag = True
			self.right(root.right, flag, rlSum)
		
t = Tree(1)
t.root.left = Node(2)
t.root.right = Node(3)
#t.root.left.left = Node(4)
#t.root.left.right = Node(5)
#t.root.right.left = Node(6)
#t.root.right.right = Node(7)
rlSum = [0]
t.right(t.root, False, rlSum)
print(rlSum[0])

				
				