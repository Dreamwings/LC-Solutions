class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.s = [0] * n
        self.s[0] = nums[0]
        for i in range(1, n):
            self.s[i] = self.s[i-1] + nums[i]
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0: return self.s[right]
        return self.s[right] - self.s[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)