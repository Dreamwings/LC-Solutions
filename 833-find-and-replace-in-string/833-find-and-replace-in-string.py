class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        ## S1: Scan from Right to Left
        
        for i, x, y in sorted(zip(indices, sources, targets), reverse=True):
            j = i + len(x)
            if s[i:j] == x:
                s = s[:i] + y + s[j:]
        
        return s