"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node: return None
        
        d = collections.defaultdict(Node)
        # d = collections.defaultdict(lambda: Node(0, None))  # both ways are good!
        root = Node(node.val)
        d[node.val] = root
        q = [node]
        
        while q:
            x = q.pop()
            x_c = d[x.val]
            
            for y in x.neighbors:
                if y.val not in d:
                    q.append(y)
                    d[y.val] = Node(y.val, [])
                
                y_c = d[y.val]
                x_c.neighbors.append(y_c)
        
        return root