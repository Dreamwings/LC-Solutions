class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n <= 1: return True
        d = '0123456789abcdefghijklmnopqrstuvwxyz'
        s = s.lower()
        i, j = 0, n - 1
        
        while i < j:
            while i < j and s[i] not in d:
                i += 1
            while i < j and s[j] not in d:
                j -= 1
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        
        
        return True    
            