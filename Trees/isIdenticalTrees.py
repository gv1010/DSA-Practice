# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class queue:
    def __init__(self):
        self.items = []
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        return self.items.pop(0)
    def isempty(self):
        return len(self.items)==0
    
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        q1 = queue()
        q2 = queue()
        if p is not None and q is not None:
            if p.val == q.val:
                q1.enqueue(p)
                q2.enqueue(q)
            else:
                return False
            
        while not q1.isempty() and not q2.isempty():
            node1 = q1.dequeue()
            node2 = q2.dequeue()
            
            if node1.left is not None and node2.left is not None:
                if node1.left.val == node2.left.val:
                    q1.enqueue(node1.left)
                    q2.enqueue(node2.left)
                else:
                    return False
                
            elif node1.left is None and node2.left is None: 
                pass
            else :
                return False
            
            if node1.right is not None and node2.right is not None:
                if node1.right.val == node2.right.val:
                    q1.enqueue(node1.right)
                    q2.enqueue(node2.right)
                else:
                    return False
                
            elif node1.right is None and node2.right is None: 
                pass
            else :
                return False
            
        return True
