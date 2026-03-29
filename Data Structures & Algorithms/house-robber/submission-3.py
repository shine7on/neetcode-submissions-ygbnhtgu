class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        maxSum = nums[0]
        cur =  nums[1]
        potential = final = 0

        for num in range(1, len(nums)):
            if num > 1:
                cur = nums[num-2] + nums[num] # + 2nd last
            if num > 2:
                potential = nums[num-3] + nums[num] # + 3rd last
            
            if potential > maxSum and potential > cur:
                maxSum = potential
                nums[num] = potential
            elif cur > maxSum:
                maxSum = cur # bigger than potential
                nums[num] = cur
        
        return maxSum

