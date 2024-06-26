class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        
        k, t = keysPressed[0], releaseTimes[0]
        
        for i in range(1, len(keysPressed)):
            time = releaseTimes[i] - releaseTimes[i-1] 
            if time > t or (time == t and keysPressed[i] > k):
                t = time
                k = keysPressed[i]
        
        return k