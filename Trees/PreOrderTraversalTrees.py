import math
import copy 
from collections import defaultdict
store = defaultdict()
class Node:
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None
	
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def print_tree(self):
		print( self.preorder_traversal(tree.root, ''))
		return True
		
	
	def preorder_traversal(self, root, traversal):
		if root:
			traversal += str(root.value) + "--"
			traversal = self.preorder_traversal(root.left, traversal)
			traversal = self.preorder_traversal(root.right, traversal)
		return traversal
	def preorderItr(self, root):
		s = []
		s.append(root)
		
		result = []
		while len(s):
			
			node = s.pop(-1)
			if len(store) == 0:
				store[node.data] = [node.data]
			
			if node.left is None and node.right is None:
				if sum(store[node.data]) == sum_val:
					result.append(store[node.data])
				
			if node.right:
				store[node.right.data] = store[node.data] + [node.right.data]
				s.append(node.right)
			if node.left:
				store[node.left.data] = store[node.data] + [node.left.data]
				s.append(node.left)
			
			
			
			#elif node.data not in store.keys():
			#	store[node.data] = store[prev.data]+[node.data]
			#
			#if node.left is None and node.right is None:
			#	store[node.data]
			#print(store)
			#print(store)	
			#if node.left is not None or node.right is not None:
			#	prev = node
			#if len(s) == 1 and flag == True:
			#	prev = root
			#	flag = False
			#print(prev.data)
		print(result)
		
	def rootToLeaf(self, root, list1 = []):
		if root is None:
			return None
		list1.append(root.data)
		print(list1)
		if sum(list1) == 8:
			return list1
		self.rootToLeaf(root.left, list1)
		self.rootToLeaf(root.right, list1)
		
			
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(8)
tree.root.left.right.right = Node(9)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
#print(tree.rootToLeaf(tree.root))
print(tree.preorderItr(tree.root))

		
	