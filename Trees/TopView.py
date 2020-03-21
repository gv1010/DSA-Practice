class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

class queue:
    def __init__(self):
        self.items = []
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        return self.items.pop(0)
    def isempty(self):
        return len(self.items) == 0
	def levelOrdertraversal(root):
		q = queue()
		val = []
		if root is not None:
			q.enqueue(root)
		while not q.isempty():
			node = q.dequeue()
			val.append(node.info)
			if node.left:
				q.enqueue(node.left)
			if node.right:
				q.enqueue(node.right)
		return val

	def vertical(root):
		save = dict()
		q = queue()
		if root:
			hd = 0
		q.enqueue(root)
		save[hd] = [root.info]
		while not q.isempty():
			node = q.dequeue()
			for k, v in save.items():
				if node.info in v:
					hd = k 
			if node.left:
				x = hd - 1
				q.enqueue(node.left)
				if x in save.keys():
					save[x].append(node.left.info)
				else:
					save[x] = [node.left.info]
			if node.right:
				x = hd + 1
				q.enqueue(node.right)
				if x in save.keys():
					save[x].append(node.right.info)
				else:
					save[x] = [node.right.info]
		return save

		

	def topView(root):
		#Write your code here
		arr = levelOrdertraversal(root)
		dict_ = vertical(root)
		#print(arr)
		#print(dict_)
		for i in sorted(dict_.keys()):
			#print(dict_[i])
			if len(dict_[i]) == 1:
				print(dict_[i][0], end = " ")
			else:
				list1 = dict_[i]
				k = []
				for j in list1:
					k.append(arr.index(j))
				k = min(k)
				print(arr[k], end = " ")
			
#sample input 
#5
#1 2 3 4 6 

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)