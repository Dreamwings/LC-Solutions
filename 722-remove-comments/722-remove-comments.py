class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        if not source: return 0
        res = []
        block_open = False
        buf = ''
        
        # if we need to count the non-space char numbers
        # def count_ch(s):
        #     cnt = 0
        #     for c in s:
        #         if c != ' ':
        #             cnt += 1
        #     return cnt

        for s in source:
            i, n = 0, len(s) 
            while i < n:
                if i - 1 < n and s[i:i+2] == '//' and not block_open:
                    break
                elif i - 1 < n and s[i:i+2] == '/*' and not block_open:
                    block_open = True
                    i += 1
                elif i - 1 < n and s[i:i+2] == '*/' and block_open:
                    block_open = False
                    i += 1
                elif not block_open:
                    buf += s[i]
                i += 1
            if buf and not block_open:
                res.append(buf)
                buf = ''

        return res        