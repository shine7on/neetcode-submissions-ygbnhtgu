class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = [0]*(len(nums)-1)

        for num in nums:
            dup[num-1] += 1
            if dup[num-1] > 1:
                return num