class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## S3:
        ## Time: O(logN)
        
        s1 = set([0, 1, 8])
        s2 = set([0, 1, 8, 2, 5, 6, 9])
        s = set()
        res = 0
        N = map(int, str(n))
        for i, v in enumerate(N):
            for j in range(v):
                if s.issubset(s2) and j in s2:
                    res += 7**(len(N) - i - 1)
                if s.issubset(s1) and j in s1:
                    res -= 3**(len(N) - i - 1)
            if v not in s2:
                return res
            s.add(v)
        return res + (s.issubset(s2) and not s.issubset(s1))
        
        """
        ## S1:
        ## Time: O(N)
        
        res = 0
        
        for i in range(1, n+1):
            s = set(str(i))
            if '3' in s or '4' in s or '7' in s:
                continue
            if '2' in s or '5' in s or '6' in s or '9' in s:
                res += 1
                
        return res
        """
        
        ## S2: DP
        ## https://leetcode-cn.com/problems/rotated-digits/solution/xuan-zhuan-shu-zi-by-leetcode/
        ## Time: O(logN)
        
        a = map(int, str(n))
        
        memo = {}
        def dp(i, equ, inv):
            if i == len(a): 
                return +(inv)
            if (i, equ, inv) not in memo:
                ans = 0
                for d in xrange(a[i] + 1 if equ else 10):
                    if d in {3, 4, 7}: continue
                    ans += dp(i+1, equ and d == a[i], inv or d in {2, 5, 6, 9})
                memo[i, equ, inv] = ans
            return memo[i, equ, inv]

        return dp(0, True, False)



        