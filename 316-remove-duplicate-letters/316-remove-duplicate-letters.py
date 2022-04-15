class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        d = {c: i for i, c in enumerate(s)}
        seen = set()
        stack = []
        
        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and stack[-1] > c and d[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
            
            stack.append(c)
            seen.add(c)
            
        return ''.join(stack)