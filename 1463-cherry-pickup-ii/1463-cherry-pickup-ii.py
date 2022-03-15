class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        ## S1: DP
        ## https://leetcode.com/problems/cherry-pickup-ii/discuss/977924/Simple-Python-14-line-DP-Top-down-no-memoization
        
        m,n = len(grid),len(grid[0])
        pos_cherry = {(0,n-1):grid[0][0]+grid[0][-1]}
        for i in range(1,m):
            new = {}
            for (x,y),val in pos_cherry.items():
                robot1 = [i for i in [x-1,x,x+1] if i>=0 and i<n]
                robot2 = [i for i in [y-1,y,y+1] if i>=0 and i<n]
                for a in robot1:
                    for b in robot2:
                        new_val = val + grid[i][a] + grid[i][b] * (a!=b)
                        if (a,b) not in new or new_val > new[(a,b)]:
                            new[(a,b)] = new_val
            pos_cherry = new
        return max(pos_cherry.values())
        