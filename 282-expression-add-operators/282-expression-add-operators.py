class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        ## S1: DFS Backtracking
        
        n = len(num)
        def dfs(pos, path, tot, pre_v):
            if pos == n:
                if tot == target:
                    res.append(path)
                return
            
            for i in range(pos, n):
                if i > pos and num[pos] == '0':  # leading 0 case, must not happend
                    break
                cur_v = int(num[pos : i+1])
                if pos == 0:  # the first number in the path, no operator
                    dfs(i+1, str(cur_v), cur_v, cur_v)
                else:
                    dfs(i+1, path + '+' + str(cur_v), tot + cur_v, cur_v)
                    dfs(i+1, path + '-' + str(cur_v), tot - cur_v, -cur_v)
                    dfs(i+1, path + '*' + str(cur_v), tot - pre_v + pre_v * cur_v, pre_v * cur_v)
        
        res = []
        dfs(0, '', 0, 0)
        return res
        