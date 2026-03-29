class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        def checkLetter(l, r, res, resLen):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print("yee")
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    print(res)
                    resLen = r - l + 1
                
                r += 1
                l -= 1
            return res, resLen

        for i in range(len(s)):
            # if its even
            l = r = i
            res, resLen = checkLetter(l, r, res, resLen)
            print(f"HERE: {resLen}")
             
            # if odd
            l = i
            r = i + 1
            res, resLen = checkLetter(l, r, res, resLen)
        
        return res