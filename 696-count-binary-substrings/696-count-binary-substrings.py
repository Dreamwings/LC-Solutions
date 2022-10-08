class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        ## S1: So Smart
        ## https://leetcode.com/problems/count-binary-substrings/discuss/108625/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation
        
        s = s.replace('01', '0 1').replace('10', '1 0').split()
        a = [] # to store the len of each element in s
        
        for sub in s:
            a.append(len(sub))
        
        res = 0
        for x, y in zip(a, a[1:]):
            res += min(x, y)
        
        return res