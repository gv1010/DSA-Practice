class Node:
	def __init__(self, val = None):
		self.val = val
		self.left = None
		self.right = None
class Tree:
	def __init__(self, root):	
		self.root = Node(root)
		
	def PathSum(self, root, target):
		
		if root is None:
			return None
		node = root
		q = [[node,[node.val]]]
		count = 0
		if node.val == target:
			count = count+1
		while len(q):
			node_list = q.pop(0)
			
			if node_list[0].left :
			
				first_l = node_list[1].copy()
				first_l.append(0)
				length = len(first_l)
				second_l = length * [node_list[0].left.val]
				sum_list_l = [x + y for x, y in zip(first_l, second_l)]
				print(sum_list_l)
				for i in sum_list_l:
					if target == i:
						count = count + 1
				q.append([node_list[0].left, sum_list_l])
			if node_list[0].right :
				
				first = node_list[1].copy()
				first.append(0)
				length = len(first)
				second = length * [node_list[0].right.val]
				sum_list = [x + y for x, y in zip(first, second)]
				print(sum_list)
				for i in sum_list:
					if target == i:
						count = count + 1
				q.append([node_list[0].right, sum_list])
		return count

		
tree = Tree(1)
tree.root.left = Node(-2)
tree.root.right = Node(-3)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(-2)
tree.root.left.left.left = Node(-1)

print(tree.PathSum(tree.root, 1))			