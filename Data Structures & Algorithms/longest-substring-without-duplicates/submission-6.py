class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == '': return 0
        start, end, leng = 0, 1, 1

        for i in range(1,len(s)):
            subs = s[start:end]
            print(subs, s[i], s[i] in subs, i)
            if s[i] in subs:
                leng = max(leng, end-start)
                print(leng, end, start)
                start = start + subs.index(s[i]) + 1
            end += 1

        return max(leng, end-start)