class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ## S1:
        ## Time: O(N)
        ## Space: O(N)
        
        end = [0] * 26 # number of subsequences ending with each letter
        M = 10**9 + 7
        
        for c in s:
            i = ord(c) - ord('a')
            end[i] = sum(end) + 1  # add 1 because c itself is also a subsequence
            
        return sum(end) % M
        
        
        