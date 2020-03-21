class Node:
	def __init__(self, val=None):
		self.val = val
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):
		self.root = Node(root)
	def compare(self,node_s, node_t):
		stack_s = []
		stack_t = []
		#flag = True
		while 1:
			while node_s and node_t:
				if node_s.val != node_t.val:
					return False
				stack_s.append(node_s)
				stack_t.append(node_t)
				node_s = node_s.left
				node_t = node_t.left
				if (node_s is None and node_t is not None) or (node_s is not None and node_t is None):
					return False
				
			if len(stack_s) == 0 and len(stack_t) == 0:
				break
			node_s = stack_s.pop()
			node_t = stack_t.pop()
			if node_s and node_t:
				node_s = node_s.right
				node_t = node_t.right
			if (node_s is None and node_t is not None) or (node_s is not None and node_t is None):
				return False
		return True
					
						
	def subTree(self, root, sub):
		node = root
		stack = []
		flag_list = []
		while (1):
			while node:
				stack.append(node)
				node = node.left
			
			if len(stack)==0:
				break
			node = stack.pop()
			if node.val == sub.val:
				flag = self.compare(node, sub)
				flag_list.append(flag)	
			node = node.right
		if True in flag_list:
			return True
		else:
			return False
				
				
tree = Tree(1)
tree.root.left = Node(1)
#tree.root.right = Node(3)
#tree.root.left.left = Node(4)
#tree.root.left.right = Node(5)
#tree.root.left.right.left = Node(6)
#tree.root.left.right.right = Node(7)

tree_1 = Tree(1)
#tree_1.root.left = Node(8)
#tree_1.root.right = Node(7)

print(tree.subTree(tree.root, tree_1.root))