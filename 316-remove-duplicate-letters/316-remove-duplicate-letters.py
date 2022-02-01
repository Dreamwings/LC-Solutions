class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ## S1: Greedy
        ## Time: O(N)
        ## https://leetcode-cn.com/problems/remove-duplicate-letters/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-4/
        ## https://leetcode.com/problems/remove-duplicate-letters/discuss/889477/Python-O(n)-greedy-with-stack-explained
        
        d = {c: i for i, c in enumerate(s)}  # store the last location of each letter
        stack = []    # non-decreasing stack to store smaller letters of the left
        seen = set()  # store ch in stack
        
        for i, c in enumerate(s):
            if c in seen: 
                continue
            while stack and stack[-1] > c and d[stack[-1]] > i:
                t = stack.pop()
                seen.remove(t)
            
            stack.append(c)
            seen.add(c)
            
        return ''.join(stack)
        """
        
        ## S2:
        ## similar to S1, but d stores ch freq
        
        d = collections.Counter(s)
        stack = []
        seen = set()
        
        for c in s:
            if c not in seen:
                while stack and stack[-1] > c and d[stack[-1]] > 0:
                    seen.remove(stack[-1])
                    stack.pop()
                    
                seen.add(c)
                stack.append(c)
            d[c] -= 1
        
        return ''.join(stack)
        """