class Node:
	def __init__(self, val = None):
		self.val = val
		self.left = None
		self.right = None
class Tree:
	#def __init__(self, root):
	#	self.root = Node(root)
			
	def Inorder(self, root):
		if root is None:
			return None
		self.Inorder(root.left)
		print(root.val, end = "-")
		self.Inorder(root.right)

def MaximumB(arr):
	if len(arr) == 1:
		return Node(arr[0])
	max_idx = arr.index(max(arr))
	max_ele = arr[max_idx]
	left_sub = arr[:max_idx]
	right_sub = arr[max_idx+1:]
	root = Node(max_ele)
	if len(left_sub) != 0:
		root.left = MaximumB(left_sub)
	if len(right_sub) != 0:
		root.right = MaximumB(right_sub)
	return root


arr = [3,2,1,6,0,5]
#main_root = Node(max(arr))
#root = main_root
root = MaximumB(arr)
tree = Tree()
tree.Inorder(root)
			