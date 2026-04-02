class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        hashS1, hashS2 = {}, {}

        for i in range(ord('a'), ord("z")+1):
            hashS1[i], hashS2[i] = 0, 0

        for char in s1:
            hashS1[ord(char)] += 1
        
        left, right = 0, len(s1)-1
        match = 0

        for i in range(left, right+1):
            hashS2[ord(s2[i])] += 1
        
        while right <= len(s2) - 1:
            for i in range(ord("a"), ord("z")+1):
                if hashS1[i] == hashS2[i]:
                    match += 1
            
            if match == 26:
                return True

            match = 0

            if right == len(s2) -1:
                return False

            left = left + 1
            right = right + 1

            lastL = s2[left - 1]
            newR = s2[right]
            hashS2[ord(lastL)] -= 1
            hashS2[ord(newR)] += 1