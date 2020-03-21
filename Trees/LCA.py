# Working
# Working
# Working
# Working
# Working
# Working

class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)
    
    
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if p == root or q==root:
            return root
        if p is not None and q is not None:
            path1 = self.search(root, p)
            path2 = self.search(root, q)
        result = []
        
        for element in path1:
            if element in path2:
                result.append(element)
            
        #for i in path1:
        #    print(i.val, end = " ")
        #    
        #print("---------------")
        #
        #for i in path2:
        #    print(i.val, end = " ")
        return result[-1] 
        #return list(set(path1) & set(path2))[-1]
        
    
    def search(self, root, key):
        q_ = Queue()
        q_.enqueue([root, [root]])
        
        while not q_.isempty():
            
            node_list = q_.dequeue()
            if node_list[0] == key:
                return node_list[1] + [node_list[0]]
            
            if node_list[0].left:
                q_.enqueue([node_list[0].left, node_list[1] + [node_list[0]]])

            if node_list[0].right:
                q_.enqueue([node_list[0].right, node_list[1] + [node_list[0]]])
                
        return None
    
    
    
    