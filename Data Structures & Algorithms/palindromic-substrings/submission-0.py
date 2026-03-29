class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def countLetter(r,l,count):
            while l >= 0 and r < len(s) and s[r] == s[l]:
                count += 1
                r += 1
                l -= 1
            return count
        

        for i in range(len(s)):
            r = l = i
            count = countLetter(r,l, count)

            l = i
            r = i + 1
            count = countLetter(r,l, count)

        return count
        
