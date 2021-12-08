class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        ## S1: 
        ## Time: O(MN)
        ## Space: O(N)
        ## https://leetcode-cn.com/problems/maximal-rectangle/solution/python3-qian-zhui-he-dan-diao-zhan-ji-su-vkpp/
        
        m, n = len(matrix), len(matrix[0])
        pre = [0] * (n + 1)
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    pre[j] += 1  # pre[j] increase by 1 from previous row
                else:
                    pre[j] = 0
            
            stack = [-1]  # mono stack to store index
            for k, x in enumerate(pre):
                while stack and pre[stack[-1]] > x:
                    idx = stack.pop()
                    h = pre[idx]
                    w = k - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(k)
        
        return res        

