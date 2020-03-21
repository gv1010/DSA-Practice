class queue:
    def __init__(self):
        self.items = []
    def enqueue(self, data):
        self.items.append(data)
    def dequeue(self):
        return self.items.pop(0)
    def isempty(self):
        return len(self.items) == 0
		
class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
		self.level = 0
		self.ver = 0
		
class Tree:
	def __init__(self, root):
		self.root = Node(root)
	
	#logic is wrong ---- 14 sept
	def TreeWidth(self, root):     
		if root is None:
			return None
		q = queue()
		level = 0
		vert = 0
		q.enqueue([root, level, vert])
		save = {}
		save[level] = [vert]
		
		while not q.isempty():
        #for node in q[:len(q)]:
			node = q.dequeue()
            #if node[0]:
           # if node[0].left is not None or node[0].right is not None:
			if node[0].left:
				vert1 = 2*node[2] 
				level1 = node[1] + 1
				q.enqueue([node[0].left, level1, vert1])
				if level1 in save.keys():
					save[level1].append(vert1)
				else:
					save[level1] = [vert1]
			if node[0].right:
				vert2 = 2*node[2] + 1
				level2 = node[1] + 1
				q.enqueue([node[0].right, level2, vert2])
				if level2 in save.keys():
					save[level2].append(vert2)
				else:
					save[level2] = [vert2]

		return save
		
		#list1 = []
		#for k, v in save.items():
		#	if len(v) > 1:
		#		list1.append(abs(v[- 1]) - abs(v[0]) + 1)
		#	elif len(v) == 1:
		#		list1.append(len(v))
		#
		#return max(list1)
				
					
					
tree = Tree(1)
tree.root.left = Node(2)
tree.root.left.left = Node(4)
tree.root.left.left.right = Node(9)

tree.root.right = Node(3)
tree.root.right.right = Node(6)
tree.root.right.right.right = Node(6)


print(tree.TreeWidth(tree.root))		
		