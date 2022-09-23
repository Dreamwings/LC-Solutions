class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter
        """
        ## S1: Heapq
        ## S2: Heapq.nlargest
        ## S3: dict.most_common(k)
        
        d = Counter(nums).most_common(k)
        return [x for x, f in d]
        
        """
        ## S4: Bucket sort
        
        d = Counter(nums)
        n = len(nums)
        b = [[] for _ in range(n+1)]  # bucket
        
        for v, f in d.items():
            b[f].append(v)
        
        res = []
        for i in range(n, -1, -1):
            if b[i]:
                res += b[i]
            if len(res) >= k:
                break
        
        return res[:k]