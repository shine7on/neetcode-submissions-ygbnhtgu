class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            
            m = l + int((r-l)/2)

            if nums[m] == target:
                return m
            elif nums[l] < target and target < nums[m]: # search left
                r = m - 1
            elif nums[l] > nums[m] and target < nums[m]:
                r = m - 1
            else: # search left
                l = m + 1

        return -1
