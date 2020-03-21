import copy
class Node:
	def __init__(self, val = None):
		self.val = val
		self.left = None
		self.right = None

class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def roottoleaf(self,root, S , result):
		if root is None:
			#print(S, end = " ")
			if sum(S) < sum(result):
				result = copy.copy(S)
				print(result)
			return result
		temp = copy.deepcopy(S)
		temp.append(root.val)
		self.roottoleaf(root.left, temp, result)
		self.roottoleaf(root.right, temp, result)
		#return result
tree = Tree(10)
tree.root.left = Node(5)
tree.root.right = Node(5)
tree.root.left.left = Node(2)
tree.root.right.right = Node(1)
tree.root.right.right.left = Node(-1)

S = []
arr = []
result = [float('inf')]
print(tree.roottoleaf(tree.root, S, result))
print(result)


		
		
		