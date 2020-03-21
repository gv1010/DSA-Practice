class Stack:
    def __init__(self):
        self.items = []
    def insert(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop(-1)
    def isempty(self):
        return len(self.items) == 0

class Node:
    def __init__(self,val = None):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self, root):
        self.root = Node(root)


    def InOrder(self,root):
        if root is None:
            return None
        s = Stack()
        p = root
        
        while 1:
            while p is not None:
                #if p.left is not None:
                s.insert(p)
                p = p.left
            #print(p)
            if s.isempty():
                break
            p = s.pop()
            print(p.val, end = " ")
            p = p.right
        #return count

tree = Tree(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)


print(tree.InOrder(tree.root))
