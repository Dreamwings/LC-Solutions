class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        
        ## S1: DP
        ## https://leetcode-cn.com/problems/minimum-cost-to-cut-a-stick/solution/qie-gun-zi-de-zui-xiao-cheng-ben-by-leetcode-solut/
        ## https://leetcode-cn.com/problems/minimum-cost-to-cut-a-stick/solution/pythondong-tai-gui-hua-dai-ma-by-xiao-dao-yu-de-pa/
        
        c = [0] + sorted(cuts) + [n]
        m = len(c) 
        f = [[float('inf')] * m for _ in range(m)]
        # f[i][j] is the total cost for all cuts between i and j
        # final result is f[0][-1] because c[0] = 0 is the start and c[m-1] = n is the end
        # for any cutting point k between i and j, the cost is:
        # f[i][j] = f[i][k] + f[k][j] + c[j] - c[i]
        # if j - i == 1, i and j are neighbors, there is no other cutting point between them
        # so f[i][i+1] = 0
        
        for i in range(m-1):
            f[i][i+1] = 0
        
        for i in range(m-1, -1, -1):
            for j in range(i+2, m):  # note that we don't consider j = i + 1 anymore
                for k in range(i+1, j):  # i + 1 <= k <= j - 1
                    cost = f[i][k] + f[k][j] + c[j] - c[i]
                    f[i][j] = min(f[i][j], cost)
        # print(f)            
        return f[0][-1]
        
        
        