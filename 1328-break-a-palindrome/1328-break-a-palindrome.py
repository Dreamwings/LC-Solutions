class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        
        ## S1:
        
        # 3 special cases and 1 general case:
        # 1. 'a'
        # 2. 'aa...aa'
        # 3. 'aba'
        # general case: 'abcba': only need to consider the left half of mid point
        
        n = len(palindrome)
        # for the general case:
        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        # for the special cases:
        if not palindrome[:-1]:
            return ''
        else:
            return palindrome[:-1] + 'b'
        
        