class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}
        l = 0
        max_len = 0

        for r in range(len(s)):
            if s[r] in window:
                window[s[r]] += 1;
                print("Updating")
            else: # until k = ok
                window.update({s[r]:1})
                print("New Char Adding")
            
            counts = list(window.values())
            max_freq = max(counts)

            while (r-l+1) - max_freq > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    window.pop(s[l])
                l += 1 # moving right
                counts = list(window.values())
            max_len = max(max_len, r-l+1)
        
        return max_len