class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    result[j] = result[j]*nums[i]

        return result
        