class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import nlargest, heappush, heappop
        
        
        ## S3: QuickSelect:
        # https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/1019513/Python-QuickSelect-average-O(n)-explained
        # Time: O(N)
        # Space: O(N)
        
        if not nums: return
        pivot = random.choice(nums)
        gt_vals = [x for x in nums if x > pivot]
        eq_vals = [x for x in nums if x == pivot]
        st_vals = [x for x in nums if x < pivot]
        
        GL, EL = len(gt_vals), len(eq_vals)
        if k <= GL:
            return self.findKthLargest(gt_vals, k)
        elif k <= GL + EL:
            return pivot
        else:
            return self.findKthLargest(st_vals, k - GL - EL)
        
        
        
        """
        ## Solution 1:
        # O(NlogK)
        
        return nlargest(k, nums)[-1]
        
        
        ## Solution 2:
        # O(NlogK)
        
        q = []
        
        for x in nums:  
            heappush(q, x)
            if len(q) > k:
                heappop(q)
        # print(q)
        return q[0]
        
        """