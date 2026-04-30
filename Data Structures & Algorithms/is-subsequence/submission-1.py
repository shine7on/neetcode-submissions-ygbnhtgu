class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True 
            
        for char in t:
            if char == s[0]:
                s = s[1:]
            if not s:
                return True
        
        return False