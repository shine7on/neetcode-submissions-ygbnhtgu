class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1

        if nums[i] < nums[j] or len(nums) == 1:
            return nums[i]

        sums = nums[i] + nums[j]

        while i <= j:
            if i == j:
                if sums <= nums[i]:
                    return nums[j+1]
                else:
                    return nums[i]

            if sums < nums[i] + nums[j]:
                return nums[j+1]
            elif sums > nums[i] + nums[j]:
                return nums[i]
            else:
                i += 1
                j -= 1
        
        return nums[i] if nums[i] < nums[j] else nums[j]