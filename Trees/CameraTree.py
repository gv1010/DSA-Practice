class Node:
	def __init__(self, val=None):
		self.val = val
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
	def Camera(self, root):
		q = [root]
		elementsCount = []
		count = 0
		while q != []:
			length = len(q)
			elementsCount.append(length)
			for _ in range(length):
				node = q.pop(0)
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			count = count + 1
	def recursive(value):
		if value > len(arr)-1:
			return None
		for i in [0,1]:
			for j in [2,3]:
				count = recursive(i+j)
		
		
		
		
tree = Tree(0)
tree.root.left = Node(0)
tree.root.right = Node(0)
tree.root.left.left = Node(0)
tree.root.left.left.left = Node(0)
tree.root.left.left.left.right = Node(0)

#tree.root.left.right = Node(0)
#tree.root.right.left = Node(6)
#tree.root.right.right = Node(7)
#tree.root.right.right.right = Node(8)
print(tree.Camera(tree.root))
		
		
		
		
		
		
		
		
		
		
		
		
			
			
		