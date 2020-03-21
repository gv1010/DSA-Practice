class Node:
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None
		
class Tree:

	def __init__(self, root):
		self.root = Node(root)
		
	def postorder_traversal(self, root, traversal):
		if root:
			traversal = self.postorder_traversal(root.left, traversal)
			traversal = self.postorder_traversal(root.right, traversal)
			traversal += (str(root.value) + '-')
		return traversal
	
	def print_traversal(self):
		print(self.postorder_traversal(self.root, ''))
		return True
		
	def postorder_iter(self, root):
		if root is None:
			return None
		q = []
		q1 = []
		node = root
		q.append(root)
		while 1:
			while node.left:
				q.append(node.left)
				node = node.left
			if len(q) == 0:
				break
			
			if node.right is None :
				print(node.value, end = " ")
				q.pop()
			node = q.pop()
			if len(q1) > 1:
				x = q1.pop()
				print(x.value,end = " ")
			if node.right:
				q1.append(node)
				node = node.right
			else:
				
				node = q.pop()
				node = node.right
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


print(tree.postorder_iter(tree.root))
		
		