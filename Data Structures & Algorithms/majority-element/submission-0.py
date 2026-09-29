class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sorting : O(nlogn) | O(1)
        nums.sort()
        return nums[len(nums)//2]