class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hashmap = {}
        longest = 0

        for index in range(len(s)):

            if s[r] not in hashmap:
                hashmap[s[r]] = 1
                r += 1
            elif hashmap[s[r]] == 0:
                hashmap[s[r]] += 1
                r += 1
            else: # duplicated
                hashmap[s[r]] += 1
                # print(hashmap)
                while hashmap[s[r]] != 1:
                    # print(l)
                    hashmap[s[l]] -= 1
                    l += 1
                r += 1
            
            longest = max(r - l, longest)
            # print(hashmap)

        
        return longest