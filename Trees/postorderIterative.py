class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
	
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def postIter(self, root):
		q = [] 
		q1 = []
		if root is None:
			return None
		node = root
		while 1 : 
			while node:
				q.append(node)
				node = node.left
				
			if len(q) == 0:
				break
			
			node = q.pop()
			
			if node in q1:
			
				#node1 = q1.pop()
				print(node.val, end = " ")
				node = None
				continue
			if node.right:

				q.append(node)
				q1.append(node)
				node = node.right
			else:
				print(node.val, end = " ")
				node = None
		return " "
				
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
#tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
#tree.root.right.right = Node(7)


print(tree.postIter(tree.root))
			
			
		
	