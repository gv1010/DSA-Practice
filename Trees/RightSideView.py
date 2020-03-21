class Node:
	def __init__(self, val = None):
		self.val = val
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root =  Node(root)
	
	def RightSide(self, root):
		result = []
		first = None
		q = [root]
		while q != []:
			length = len(q)
			for _ in range(len(q)):
				node = q.pop(0)
				print(node.val)
				if node.right:
					q.append(node.right)
				if node.left:
					q.append(node.left)
				if first is None:
					first = node.val
			result.append(first)
			first = None
		return result
	def Diameter(self, root):
		if root is None:
			return 0
		L_height = self.Diameter(root.left)
		R_height = self.Diameter(root.right)
		return 1+ max(L_height, R_height)
			
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.Diameter(tree.root))

					
				
			