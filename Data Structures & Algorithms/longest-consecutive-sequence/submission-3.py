class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()

        curr = 1
        longest = 1

        prev = nums[0]

        for num in nums:
            if num == prev + 1:
                curr += 1
            elif num == prev:
                curr = curr
            else:
                curr = 1
            
            prev = num
            if curr > longest:
                longest = curr
        
        return longest
            

                
        