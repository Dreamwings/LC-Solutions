class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        res = []
        i, carry = len(num) - 1, 0
        while i >= 0 or k != 0:
            x = num[i] if i >= 0 else 0
            y = k % 10 if k != 0 else 0

            sum = x + y + carry
            res.append(sum % 10)
            carry = sum // 10

            i -= 1
            k //= 10
        if carry != 0: res.append(carry)
        return res[::-1]


