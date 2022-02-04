"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        from collections import defaultdict
        
        
        if not node: return None
        
        ## Copy reference node first with empty neighbors
        d = defaultdict(lambda: Node(0, None))
        root = Node(node.val, [])
        d[node.val] = root
        q = [node]
        
        while q:
            x = q.pop()
            xc = d[x.val]
            
            for y in x.neighbors:
                if y.val not in d:
                    q.append(y)
                    d[y.val] = Node(y.val, [])
                
                yc = d[y.val]
                xc.neighbors.append(yc)
        
        return root