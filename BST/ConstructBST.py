class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
class Tree:
	def __init__(self, root = None):
		self.root = Node(root)
		
	def bst(self,arr):
		if len(arr) == 1:
			return Node(arr[0])
		
		if len(arr) != 0:
			index = int(len(arr)/2)
			root = Node(arr[index])
			root.left = self.bst(arr[:index])
			root.right = self.bst(arr[index+1:])
			return root
		
		
	def inorder(self, root):
		if root is None:
			return None
		self.inorder(root.left)
		print(root.data, end = " ")
		self.inorder(root.right)
		
arr = [2,3,4,5,6,7,8]
tree = Tree(None)
root = tree.bst(arr)

print(tree.inorder(root))


	