class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        l = 0
        res = 0

        # go through the string input
        for r in range(len(s)):
            # go through the set 
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, r - l + 1)

        return res



            