class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        from collections import Counter
        from heapq import nlargest, heappush, heappop
        
        ## S4: Bucket Sort
        
        d = Counter(nums)
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        
        for x, freq in d.items():
            bucket[freq].append(x)
        
        # flat_list = list(itertools.chain(*bucket))
        # return flat_list[::-1][:k]
        # print(bucket)
        res = []
        for i in range(n, -1, -1):
            if bucket[i]:
                res += bucket[i]
            if len(res) >= k:
                break
                
        return res[:k]
        
        """
        ## Solution 1:
        
        d = Counter(nums)
        
        freq = []
        
        for key, v in d.items():
            freq.append((v, key))
        
        freq = nlargest(k, freq)
        
        res = [y for x, y in freq]
        
        return res[:k]
        
        
        ## Solution 2:
        
        d = Counter(nums)
        freq = [(v, key) for key, v in d.items()]
        
        res = []
        for v, num in freq:
            heappush(res, (v, num))
            if len(res) > k:
                heappop(res)
        
        return [y for x, y in res]
        
        
        ## Solution 3:
        
        d = Counter(nums).most_common(k)
        
        return [x for x, v in d]
        """