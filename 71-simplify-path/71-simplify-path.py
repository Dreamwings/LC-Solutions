class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stack = []
        a = [x for x in path.split('/') if x != '' and x != '.']
        
        for c in a:
            if c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        return '/' + '/'.join(stack)
        
        """
        
        stack = []
        
        for c in path.split('/'):
            if c == '.':
                continue
            elif c == '':
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        
        return '/' + '/'.join(stack)
        """