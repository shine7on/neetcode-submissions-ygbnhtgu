class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS, hashT = {}, {}

        if len(s) != len(t):
            return False

        for char in s:
            if hashS.get(char) == None:
                hashS[char] = 1
            else: 
                hashS[char] += 1

        for char in t:
            if hashT.get(char) == None:
                hashT[char] = 1
            else: 
                hashT[char] += 1
        
        return hashS == hashT
