class Solution(object):
    def totalStrength(self, strength):
        """
        :type strength: List[int]
        :rtype: int
        """
        n = len(strength)
        M = 10 ** 9 + 7
        if n == 1: return strength[0] * strength[0] % M

        res = 0
        s, stack, acc = 0, [-1], [0]
        strength.append(0)

        for r, x in enumerate(strength):
            s += x
            acc.append(s + acc[-1])
            while stack and strength[stack[-1]] > x:
                i = stack.pop()
                l = stack[-1]
                lacc = acc[i] - acc[max(l, 0)]
                racc = acc[r] - acc[i]
                ln, rn = i - l, r - i
                res += strength[i] * (racc * ln - lacc * rn) % M
            stack.append(r)
        
        return res % M