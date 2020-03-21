import copy
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		self.first = []
		
	#def isBST(self, root, lower = float('-inf'), higher = float('inf')):
	#	if root is None:
	#		return True
	#	if not lower <= root.data <= higher:
	#		print(root.data, end = " ")
	#		self.first.append(root)
	#	self.isBST(root.left, lower, root.data)
	#	self.isBST(root.right, root.data, higher)
	#	
	#def Restore(self, root):
	#	self.isBST(root, lower = float('-inf'), higher = float('inf'))
	#	temp = self.first[0].data
	#	self.first[0].data = self.first[1].data 
	#	self.first[1].data = temp
	#	return root
		
	def inorder(self, root):
		
		node = root
		q = []
		prev_node = Node(-999)
		count = 0
		while 1:
			while node:
				q.append(node)
				node = node.left
					
			if q == []:
				if count == 1:
					temp3 = next_to_prev.data
					print(next_to_prev.data)
					next_to_prev.data = temp1.data
					print(temp1.data)
					temp1.data = temp3
					break
				else:
					break
					
			node = q.pop()
			
			if count == 1 and not prev_node.data < node.data:
				temp2 = node.data
				node.data = temp1.data
				temp1.data = temp2
				count = count + 1
			
			if count == 0 and not prev_node.data < node.data:
				temp1 = prev_node
				next_to_prev = node
				prev_node = node
				count = count + 1	
			
			if prev_node.data < node.data:
				prev_node = node
			
			print(node.data, end = "-")
			node = node.right
			
tree = Tree(10)
tree.root.left = Node(15)
tree.root.right = Node(14)
#tree.root.right.right = Node(15)
tree.root.left.left = Node(4)
tree.root.left.right = Node(8)
#tree.root.right.left = Node(5)
tree.root.right.right = Node(7)
#tree.root.right.right.right = Node(9)	
#tree.inorder(tree.root)
print()
#tree.isBST(tree.root, lower = float('-inf'), higher = float('inf'))
print()
#tree.Restore(tree.root)
print()
tree.inorder(tree.root)