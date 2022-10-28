class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        q = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1
        
        while q:
            x, y = q.popleft()
            for dx, dy in dir:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and mat[i][j] < 0:
                    q.append((i, j))
                    mat[i][j] = 1 + mat[x][y]
        
        return mat            