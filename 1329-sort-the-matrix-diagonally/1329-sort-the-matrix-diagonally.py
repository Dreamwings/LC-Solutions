class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m, n = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                d[i-j].append(mat[i][j])
        
        for k in d:
            d[k].sort(reverse=True)
        
        for i in range(m):
            for j in range(n):
                k = i - j
                mat[i][j] = d[k].pop()
        return mat