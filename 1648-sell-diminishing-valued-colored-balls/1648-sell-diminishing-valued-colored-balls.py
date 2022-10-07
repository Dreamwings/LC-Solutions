class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        
        ## S2:
        ## https://leetcode.com/problems/sell-diminishing-valued-colored-balls/discuss/927522/Python-n-log-n-690-ms
        
        from collections import Counter
        
        arr=sorted(Counter(inventory).items(), reverse=True)+[(0,0)]
        ans, ind, width=0,0,0
        
        while orders>0:
            width += arr[ind][1]
            sell=min(orders, width * (arr[ind][0] - arr[ind+1][0]))
            whole, remainder= divmod(sell, width)
            ans += width*(whole*(arr[ind][0]+arr[ind][0]-(whole-1)))//2 + remainder*(arr[ind][0]-whole)
            orders -= sell
            ind += 1
        return ans % (10**9 + 7)
        
        
        """
        ## S1: Time Limit Exceeded
        
        from heapq import heappush, heappop
        
        a, res = [], 0
        
        for x in inventory:
            heappush(a, -x)
        
        for _ in range(orders):
            x = -heappop(a)
            res += x
            res %= (10**9 + 7)
            x -= 1
            heappush(a, -x)
        
        return res
        """