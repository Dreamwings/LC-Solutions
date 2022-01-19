class Solution:
    def knightDialer(self, n: int) -> int:
        
        ## S2:
        ## Time: O(logN)
        ## Space: O(1)
        
        import numpy as np
        
        K = 10**9 + 7
        M = np.matrix([ [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])        
        x = np.matrix([1] * 10) 
        N = n - 1
        
        while N:
            if N % 2:  # N odd
                x = (x * M) % K
                N -= 1
            M = (M * M) % K
            N //= 2
        
        return np.sum(x) % K
        
        """
        ## S1:
        ## Time: O(N)
        ## Space: O(1)
        
        x = [1] * 10
        # x[i] means current total count when knight is at i, i is 0, 1, ..., 9
        K = 10**9 + 7
        
        for i in range(n-1): # jump n-1 steps
            y = [x[4] + x[6],  # you can jump from 4 or 6 to 0, so the total for next 0 state will be the sum of current 4 and 6
                 x[6] + x[8],
                 x[7] + x[9],
                 x[4] + x[8],
                 x[0] + x[3] + x[9],
                 0,
                 x[0] + x[1] + x[7],
                 x[2] + x[6],
                 x[1] + x[3],
                 x[2] + x[4]
                ]
            x = y
        
        return sum(x) % K
        
        """
        
        
        