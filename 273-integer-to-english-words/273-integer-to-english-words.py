class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        """
        ## S0:
        from num2words import num2words
        return num2words(num)
        """
        ## S2:
        
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
            if x < 20:
                return lt20[x-1:x]
            if x < 100:
                q, r = x // 10, x % 10
                return [tens[q-2]] + helper(r)
            if x < 1000:
                q, r = x // 100, x % 100
                return [lt20[q-1]] + ['Hundred'] + helper(r)
            
            for p, w in enumerate(thsd):
                if x < 1000 ** (p + 1):
                    t = 1000 ** p
                    q, r = x // t, x % t
                    return helper(q) + [w] + helper(r)
        
        if num == 0: return 'Zero'
        return ' '.join(helper(num))
        
        """