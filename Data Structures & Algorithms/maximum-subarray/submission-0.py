class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0];
        curSum = 0;

        # if theres negative prefix, remove that
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        
        return maxSub