class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        a, b = [], []
        
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                a.append(i)
                if i * i != n:
                    b.append(n // i)
            
        la, lb = len(a), len(b)
        if k > la + lb:
            return -1
        elif k <= la:
            return a[k-1]
        else:
            x = k - la
            return b[-x]
        
        