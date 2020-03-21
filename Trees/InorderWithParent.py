class Node:
	def __init__(self, data =None):
		self.data = data
		self.parent = None
		self.left = None
		self.right = None

class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def Inorder(self, root):
		 node = root
		 buff = []
		 while 1:
			while node.left:
				node =  node.left
				
			buff.append(node)
			if node.right:
				node = node.right
			if node.right is None:
				print(node.val, end = " ")
				node = node.parent
				if node in buff:
				
				node = node.right
				
	def inorder-traversal (tree) :
		prev, result = None, []
		while tree:
			if prev is tree. parent:
			# We came down to tree from prev,
				if tree. left: # Keep going 7eft.
				nert = tree. left
				else:
				result . append (tree . data)
				# Done with left , so go right if right is not enpty
				# go up.
				nert = tree.right or tree.parent
				elif tree.left is prev:
			# lle cane up to tree fron its TeIt child.
			result . append(tree. data)
			# Done with 7eft, so go right if right is not enpty
			# up.
			next = tree.right or tree.parent
			else: # Done with both children, so nove up,
			nelt = tree. parent
			Otherwise, go
			prev, tree = tree, nelt
			return result
				
				
		