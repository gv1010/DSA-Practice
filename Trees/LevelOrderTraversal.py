class Queue:
    def __init__(self):
        self.items = []
 
    def isempty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
		
class Node:
	def __init__(self, value = None):
		self.val = value
		self.left = None
		self.right = None
		
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		
	def levelorder(self, root):
		if root is None:
			return None
			
		q = Queue()
		q.enqueue(root)
		traversal = "-"
		while not q.isempty():
			node = q.dequeue()
			temp = node.right
			node.right = node.left
			node.left = temp
			
			#traversal += str(node.value) + '-'
			if node.left:
				q.enqueue(node.left)
			if node.right:
				q.enqueue(node.right)
		#return traversal
		return root
	def inorder(self, root):
		if root is None:
			return None
		self.inorder(root.left)
		print(root.value, end = "-")
		self.inorder(root.right)
	
	def level(self, root):
		if root is None:
			return None
		q = []
		save = {}
		level = 0
		q.append(root)
		while len(q):
			length = len(q)
			level = level + 1
			sum_ = 0
			for __ in range(length):
				node = q.pop(0)
				sum_ = sum_ + node.val
				
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			save[level] = sum_
		even = 0
		odd = 0
		for key in save.keys():
			if key % 2 :
				even = even + save[key]
			else:
				odd = odd + save[key]
		return max(even, odd)
	def levelOrder(self, root, x , y ):	
		node = root
		q = []
		q.append(node)
		
		while len(q):
			parent_x = None
			parent_y = None
			length = len(q)
			
			for i in range(length):
				node = q.pop(0)
				print(node.val, end = " ")
				if node.left:
					q.append(node.left)
					if parent_x is None and node.left.val == x:
						parent_x = node
					elif parent_y is None and node.left.val == y:
						parent_y = node
					
				if node.right:
					q.append(node.right)
					if parent_x is None and node.right.val == x:
						parent_x = node
					elif parent_x is None and node.right.val == y:
						parent_y = node
			if parent_x is not None and parent_y is not None and parent_x != parent_y:
				return True
		return False
			
				
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(5)
#tree.root.left.right = Node(5)
#tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.leftleft = Node(8)
#tree.root.left.right = Node(5)
#print(tree.inorder(tree.root))
#invert_root = tree.levelorder(tree.root)
#print(tree.inorder(invert_root))
print(tree.levelOrder(tree.root, x= 5, y=7))		
		