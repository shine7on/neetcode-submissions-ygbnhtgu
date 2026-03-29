class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for num in range(1, len(nums)):
            prev = nums[num-1]
            if prev == nums[num]:
                return True
        return False
