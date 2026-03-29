class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def subRob(li):
            rob1 = rob2 = 0
            for n in li:
                temp = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max (subRob(nums[:-1]), subRob(nums[1:]))
