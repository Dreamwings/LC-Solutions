"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        
        ## Solution 1: DFS
        
        
        from collections import defaultdict
        
        d_imp = defaultdict(int)
        d_sub = defaultdict(list)
        
        for x in employees:
            d_imp[x.id] = x.importance
            d_sub[x.id] = x.subordinates
        
        # print(d_imp)
        # print(d_sub)
        
        res = 0
        q = [id]
        
        while q:
            i = q.pop()
            res += d_imp[i]
            for j in d_sub[i]:
                q.append(j)
        
        return res
        