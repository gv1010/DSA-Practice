class Node:
	def __init__(self, val = None):
		self.val = val
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
	def Flatten(self, root):
		node = root
		stack = [node]
		prev = None
		while 1:
			if stack == []:
				break
			node = stack.pop(-1)
			if node.right :
				stack.append(node.right)
			if node.left :
				stack.append(node.left)
			if prev != None:
				prev.right = node
				prev.left = None
				prev = node
			else:
				prev = node
		return root
	def print_preorder(self, root):
		if root is None:
			return None
		print(root.val)
		self.print_preorder(root.left)
		self.print_preorder(root.right)
		
		
class BSTIterator:

	def __init__(self, root):
		self.stack = []
		self.helper(root)
		
	def helper(self, root):
		while root:
			self.stack.append(root)
			root = root.left

	def next(self):
		"""
		@return the next smallest number
		"""
		value = self.stack.pop(-1)
		if value.right:
			self.helper(value.right)
		return value.val

	def hasNext(self):
		"""
		@return whether we have a next smallest number
		"""
		return len(self.stack) > 0
		
        


			
tree = Tree(7)
tree.root.left = Node(3)
tree.root.right = Node(15)
tree.root.right.left = Node(9)
tree.root.right.right = Node(20)
#tree.root= Node(6)
#tree.root = Node(7)

#trans =  tree.Flatten(tree.root)
obj = BSTIterator(tree.root)
print(obj.hasNext())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())



			