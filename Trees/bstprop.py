class Tree:
	def __init__(self, root):
		self.root = Node(root)
class Node:
    def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def inorder(root1, list1):
	if root1 is None:
		return None
	inorder(root1.left, list1)
	list1.append(root1.data)    
	inorder(root1.right, list1)
	return list1
    
def check_binary_search_tree_(root):
	list1 = []
	if root:
		output = inorder(root, list1)
		print(output)
	else:
		return True
	   #print(root.data
		print(output)
		if len(set(output)) != len(output):
		   return False
		if len(output) == 0 or output == sorted(output):
		   return True
		else:
		   return False

tree = Tree(None)
#tree.root.left = Node(2)
#tree.root.right = Node(3)
#tree.root.left.left = Node(4)
#tree.root.left.right = Node(5)
#tree.root.right.left = Node(6)
#tree.root.right.right = Node(7)

print(check_binary_search_tree_(tree.root))