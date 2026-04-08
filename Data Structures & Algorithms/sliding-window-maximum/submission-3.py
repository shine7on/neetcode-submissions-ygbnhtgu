class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left, right = 0, k
        res = []

        for right in range(k,len(nums)+1):
            sub = nums[left:right]
            res.append(max(sub))
            left += 1

        return res