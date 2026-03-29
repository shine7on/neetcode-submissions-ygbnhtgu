class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) < 2):
            return null

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j] == target):
                    return [i,j]            