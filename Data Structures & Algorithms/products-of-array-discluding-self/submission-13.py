class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = 1
        result.append(1)

        i = 0

        while len(result) != len(nums):
            prefix *= nums[i]
            result.append(prefix)
            i += 1
        
        postfix = 1
        
        for j in range(len(nums)-1,0,-1):
            postfix *= nums[j]
            result[j-1] *= postfix
        
        return result


        