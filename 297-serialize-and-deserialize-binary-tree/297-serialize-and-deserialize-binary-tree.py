# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    ## S1: DFS
    
    def serialize(self, root):
        
        vals = []
        def dfs(root):
            if root:
                vals.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
            else:
                vals.append('$')
        
        dfs(root)
        return ','.join(vals)
        

    def deserialize(self, data):
        
        data = data.split(',')
        vals = iter(data)
        
        def dfs():
            x = next(vals)
            if x == '$':
                return None
            root = TreeNode(x)
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
        
    """
    ## S2: BFS
    
    from collections import deque
    
    def serialize(self, root):
        
        if not root: return ''
        res = []
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('$')
        
        return ','.join(res)
        

    def deserialize(self, data):
        
        if not data: return None
        
        vals = data.split(',')
        root = TreeNode(vals[0])
        i, n = 1, len(vals)
        q = deque([root])
        
        while q:
            node = q.popleft()
            if vals[i] != '$':
                node.left = TreeNode(vals[i])
                q.append(node.left)
            i += 1
            if vals[i] != '$':
                node.right = TreeNode(vals[i])
                q.append(node.right)
            i += 1
                
        return root
    
    """    
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))