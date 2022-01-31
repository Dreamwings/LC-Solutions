class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        ## S1: Topological Sort
        ## Time: O(N)
        ## Space: O(N)
        
        indeg = {x:0 for x in range(n)}
        ch = set(leftChild + rightChild)
        
        for i in range(n):
            if i in ch:
                indeg[i] += 1
                
        q = collections.deque()
        seen = set()
        for k, v in indeg.items():
            if v == 0:
                q.append(k)
                
        if len(q) == 0 or len(q) > 1: 
            # there is a cycle, or two roots
            return False
        
        while q:
            x = q.popleft()
            if x in seen:  # there must be a cycle
                return False
            seen.add(x)
            
            if leftChild[x] != -1:
                q.append(leftChild[x])
            if rightChild[x] != -1:
                q.append(rightChild[x])
                
        return len(seen) == n