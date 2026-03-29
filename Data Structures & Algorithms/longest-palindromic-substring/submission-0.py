class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        for i in range(len(s)):
            # if its even
            l = r = i
            print(l, r)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print('yey')
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                r += 1
                l -= 1
            
            # if odd
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                r += 1
                l -= 1
        
        return res

'''
        def checkLetter(l, r):
            while l > 0 and r > len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                r += 1
                l -= 1
                '''
            
                
            
