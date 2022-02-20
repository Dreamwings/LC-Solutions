class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        ## S1: Sort
        ## https://leetcode.com/problems/car-fleet/discuss/139850/C%2B%2BJavaPython-Straight-Forward
        ## https://leetcode-cn.com/problems/car-fleet/solution/che-dui-by-leetcode/
        ## Time: O(NlogN)
        ## Space: O(N)
        
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        res = k = 0
        # k is the needed time for the closest fleet in front of the current car
        
        for t in times[::-1]:
            if t > k: 
                # means the current car can NOT catch up the fleet in front of it
                # it must be a new fleet
                res += 1
                k = t
            
        return res
        
        
        