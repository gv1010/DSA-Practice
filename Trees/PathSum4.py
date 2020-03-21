class Node:
	def __init__(self, val = None):
		self.val = val
		self.left = None
		self.right = None
	
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		self.store = dict()
		self.parent = dict()
		
	def func(self, root):
		def pathSum(root):
			if root is None:
				return float('-inf'),float('-inf'), 0
				
			ln, lp, nvl = pathSum(root.left)
			rn, rp, nvr = pathSum(root.right)
			return max(root.val + nvl, root.val+ nvr, root.val+nvl+nvr, ln,rn) , max(root.val+max(lp, rp), root.val), root.val
		
				
		node, path, val = pathSum(root.left)
		node_, path_, val_ = pathSum(root.right)
		
		if path == float('-inf'):
			path = 0
		if path_ == float('-inf'):
			path_ = 0
		if node == float('-inf'):
			node = 0
		if node == float('-inf'):
			node_ = 0

		return max(max(node, node_), max(path_, path), path_ + path + root.val)
		
			#if root.left and root.right is None:
			#	node = root.val + root.left.val
			#elif root.right and root.left is None:
			#	node = root.val + root.right.val
			#elif root.left and root.right:
			#	node = root.val + root.right.val + root.left.val
			#else:
			#	node = root.val
			#if node < max(ln, rn) :
			#	node = max(ln, rn)

		
#tree = Tree(5)
#tree.root.left = Node(4)
#tree.root.right = Node(8)
#tree.root.right.left = Node(13)
#tree.root.right.right = Node(4)
#tree.root.right.right.right = Node(1)
#tree.root.left.left = Node(11)
#tree.root.left.left.left = Node(7)
#tree.root.left.left.right = Node(2)

#tree = Tree(5)
#tree.root.left = Node(-5)
#tree.root.right = Node(-9)
#tree.root.right.left = Node(2)
##tree.root.right.right = Node(4)
##tree.root.right.right.right = Node(1)
#tree.root.left.left = Node(6)
#tree.root.left.right = Node(3)
#tree.root.left.right.left = Node(5)
#tree.root.left.right.right = Node(4)
#tree.root.left.right.right.right = Node(1)
##tree.root.left.left.left = Node(7)
#tree.root.left.left.right = Node(2)

#tree = Tree(-1)
#tree.root.left = Node(8)
#tree.root.right = Node(2)
#tree.root.right.left = Node(0)
##tree.root.right.right = Node(7)
##tree.root.left.left = Node(1)
#tree.root.left.right = Node(-9)
#tree.root.right.left.left = Node(-3)
#tree.root.right.left.left.right = Node(-9)
#tree.root.right.left.left.right.right = Node(2)
##tree.root.right.left.left.right.right = Node(2)

tree = Tree(2)
tree.root.left = Node(1)
#tree.root.right = Node(15)
###tree.root.left.left = Node(2)
###tree.root.left.right = Node(3)
#tree.root.right.left = Node(20)
#tree.root.right.right = Node(7)
print(tree.func(tree.root))
