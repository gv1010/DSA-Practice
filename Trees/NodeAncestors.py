class Node:
	def __init__(self, val = None):
		self.val = val
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
	
	def ancestors(self, root, nodeVal, list1 = []):
		if root is None:
			return
		
		list1.append(root.val)
		#print(list1)
		if root.val == nodeVal:
			#print(list1)
			return list1
		else:
			self.ancestors(root.left,nodeVal ,list1)
			self.ancestors(root.right,nodeVal ,list1)
			
	def printfun(self, list1):
		for i in list1:
			print(i, end = " ")
			
			
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.left.left = Node(6)
tree.root.left.right.right = Node(7)

print(tree.ancestors(tree.root, 3, []))