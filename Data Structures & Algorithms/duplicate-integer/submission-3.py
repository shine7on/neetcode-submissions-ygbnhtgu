class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums) == 0):
            return False

        nums.sort()

        self = nums[0]

        for num in range(1, len(nums)):
            if self == nums[num]:
                return True
            self = nums[num]

        return False