class Solution:
    def scoreOfString(self, s: str) -> int:

        prev = ord(s[0])
        res = 0
        
        for i in range(1,len(s)):
            res += abs(ord(s[i])-prev)
            prev = ord(s[i])

        return res
