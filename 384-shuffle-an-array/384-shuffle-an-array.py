class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d = nums[:]
        

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.d
        

    def shuffle(self):
        """
        :rtype: List[int]
        """
        ## S1: 
        arr = self.d[:]
        random.shuffle(arr)
        return arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()