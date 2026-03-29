class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        length = len(s)
        dic = {}

        for x in range(0,length):
            if dic.get(s[x]) is None:
                dic.update({s[x]:1})
            else:
                count = dic.get(s[x]) + 1
                dic.update({s[x]:count})
        
        for y in range(0,length):
            if dic.get(t[y]) is None or dic.get(t[y]) <= 0:
                return False
            else: 
                count = dic.get(t[y]) - 1
                dic.update({t[y]:count})

        return True
        