class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        from collections import defaultdict
        
        s = defaultdict(int)
        
        for a in nums1:
            for b in nums2:
                s[a + b] += 1
        
        res = 0
        for c in nums3:
            for d in nums4:
                x = -(c + d)
                if x in s:
                    res += s[x]
        
        return res