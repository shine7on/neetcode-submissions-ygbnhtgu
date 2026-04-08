class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxleng = 0
        left, right, cur = 0, 0, ''
        count = k
        hashmap = {}

        for right in range(len(s)):
            hashmap[s[right]] = 1 + hashmap.get(s[right],0)
            
            while (right-left+1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1
            
            maxleng = max(right-left+1, maxleng)
        return maxleng
