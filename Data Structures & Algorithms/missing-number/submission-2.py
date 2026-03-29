class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()

        for i in range(length):
            if i != nums[i]:
                return i
        
        return length