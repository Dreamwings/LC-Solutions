class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed))
        times = [1.0 * (target - p)/s for p, s in cars]
        # print(cars, times)
        prev = 0
        res = 0
        
        for t in times[::-1]: # consider the one closest to the target first
            if t > prev: # current car need more time than the prev one, not catch up
                res += 1
                prev = t
        
        return res
        