class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
class Tree:
	def __init__(self, root):
		self.root = Node(root)
		self.flag = True
	def isHeap(self, root):
		if root is None:
			return None
		if root.left is None and root.right is None:
			return
		self.isHeap(root.left) 
		self.isHeap(root.right)
		if not root.data > root.left.data and root.data> root.right.data:
			self.flag = False
		else:
			return self.flag
		
tree = Tree(7)
tree.root.left = Node(3)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(2)
tree.root.right.left = Node(8)
tree.root.right.right = Node(4)

#print(tree.isHeap(tree.root))


def zeross(numb):
	def zeros(numb, count = 0):
		
		if numb == 0:
			return 0
		count = zeros(int(numb/10), count)
		if numb%10 == 0:
			count = count + 1
		return count
	return zeros(numb, 0)
	
#numb = int(input())
#print(zeross(numb))
def geo(k):
	if k == 0:
		return 1.0
	sum1 = (1/pow(2, k)) + (geo(k-1))
	return sum1

k = int(input())
print(geo(k))
