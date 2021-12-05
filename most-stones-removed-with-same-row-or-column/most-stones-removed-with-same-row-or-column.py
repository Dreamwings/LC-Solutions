class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        
        ## S1: Union Find
        ##
        ## https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/python3-bing-cha-ji-lian-jie-heng-zong-z-e3kc/
        ## https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/197668/Count-the-Number-of-Islands-O(N)
        
        n = 10010  # as xi, yi <= 10000
        p = list(range(2*n))  # n xi, n yi to store parent nodes
        
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            p[find(x)] = p[find(y)]
        
        # to connect y axis
        for i, j in stones:
            union(i, j + n)
        
        # get all root for unioned nodes
        root = set()
        
        for i, j in stones:
            root.add(find(i))
        
        return len(stones) - len(root)
        
        
        