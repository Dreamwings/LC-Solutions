class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        ## S1:
        ## https://leetcode.com/problems/robot-bounded-in-circle/discuss/290856/JavaC%2B%2BPython-Let-Chopper-Help-Explain
        ## Time: O(N)
        ## Space: O(1)
        
        x, y = 0, 0
        dx, dy = (0, 1)  # initialize the original direction to face north
        
        for X in instructions:
            if X == 'L':
                dx, dy = -dy, dx  # refer to the yellow figure in the above link
            if X == 'R':
                dx, dy = dy, -dx  # refer to the yellow figure in the above link
            if X == 'G':
                x, y = x + dx, y + dy
        
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
        
        