class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        from collections import Counter
        
        d = Counter(tasks)
        M = max(d.values())
        num = 0 # num of tasks with frequency of M
        
        for k, v in d.items():
            if v == M:
                num += 1
        
        
        x = len(tasks)  # when M is small compared with x, there are many different tasks, meet n easily
        y = (M - 1) * (n + 1) + num  # M is large, need to add idle periods
        
        return max(x, y)