class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        
        from collections import Counter
        
        ## S3:
        ## Time: O(N)
        
        dt = Counter(target)
        da = Counter(arr)
        
        for k, v in dt.items():
            if k not in da:
                return False
            elif da[k] != v:
                return False
                
        return True
    
        """
        ## S1: 
        ## Time: O(N*logN)
        
        return sorted(arr) == sorted(target)
        
        
        ## S2:
        ## Time: O(N)
            
        d = Counter(target)
        
        for x in arr:
            d[x] -= 1
            if d[x] < 0:
                return False
        
        return True
        
        """