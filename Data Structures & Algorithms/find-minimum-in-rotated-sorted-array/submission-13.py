class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1

        while start < end:
            mid = (end - start) // 2 + start 
            gapLeft, gapRight = nums[mid] - nums[start], nums[end] - nums[mid]
            print(gapLeft, gapRight)
            if end - start == 1:
                return nums[start] if nums[start] < nums[end] else nums[end]

            if gapLeft > 0 and gapRight > 0:
                return nums[start]     
            elif gapLeft < 0:
                end = mid
            else:
                start = mid
        
        return nums[start]