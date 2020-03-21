class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
class Tree:
	def __init__(self,root):
		self.root = Node(root)
	
	def level(self, nums):
		if len(nums) == 1:
			return Node(nums[0])
		val = nums.pop(0)
		root = Node(val)
		left = []
		right = []
		for i in nums:
			if i < val:
				left.append(i)
			else:
				right.append(i)
		root.left = self.level(left)
		root.right = self.level(right)
		return root
		
	def inorder(self, root):	
		if root is None:
			return None
		print(root.data, end = " ")
		self.inorder(root.left)
		
		self.inorder(root.right)
		
		
arr = [6,4,10,2,5,8,11]
print(arr)
tree = Tree(None)
root = tree.level(arr)
print(tree.inorder(root))
