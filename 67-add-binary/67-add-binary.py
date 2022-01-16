class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        ## Solution 1:
        
        i, j, s, c = len(a) - 1, len(b) - 1, 0, 0
        res = ''
        
        while i >= 0 or j >= 0 or c:
            s = c
            if i >= 0:
                s += int(a[i])
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -= 1
            
            c = s // 2
            res += str(s % 2)
            
        return res[::-1]
            
        """
        
        ## Solution 2:
        return str(bin(int(a, 2) + int(b, 2)))[2:]
        """
        