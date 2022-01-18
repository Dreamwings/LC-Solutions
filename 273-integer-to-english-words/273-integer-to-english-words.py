class Solution:
    def numberToWords(self, num: int) -> str:
        
        ## S2:
        ## https://leetcode.com/problems/integer-to-english-words/discuss/164087/Python-100-and-Easy-To-Understand-Solution
        
        d = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
             16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty',
             30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
             80: 'Eighty', 90: 'Ninety', 100: 'Hundred',
             1000: 'Thousand', 1e6: 'Million', 1e9: 'Billion'}
        
        dr = [10**9, 10**6, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20]
        
        def f(n):
            if n <= 20:
                return d[n]
            
            for x in dr:
                q, r = n // x, n % x
                if not q:
                    continue
                
                a, b = '', ''
                if x >= 100:
                    a = f(q) + ' '
                if r:
                    b = ' ' + f(r)
                return a + d[x] + b
        
        return f(num)
       
        """
        ## S1:
        
        lt20 = ["One","Two","Three","Four","Five","Six","Seven","Eight", \
                "Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen", \
                "Sixteen", "Seventeen","Eighteen","Nineteen"]
        tens = ["Twenty","Thirty","Forty","Fifty", \
                "Sixty","Seventy","Eighty","Ninety"]
        thsd = ["","Thousand","Million","Billion","Trillion"]
        
        def helper(x):
            # return an array of English words
            if x < 20:
                return lt20[x-1:x]
            if x < 100:
                a, b = x // 10, x % 10
                return tens[a-2:a-1] + helper(b)
            if x < 1000:
                a, b = x // 100, x % 100
                return [lt20[a-1]] + ['Hundred'] + helper(b)
            
            for i, v in enumerate(thsd):
                if x < 1000 ** (i + 1):
                    t = 1000 ** i
                    a, b = x // t, x % t
                    return helper(a) + [v] + helper(b)
         
        if num == 0: return 'Zero'
        res = helper(num)
        return ' '.join(res)
        """    
       