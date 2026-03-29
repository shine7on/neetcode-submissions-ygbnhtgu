class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for x in range(len(nums)):
            remain = target - nums[x]
            if hashmap.get(remain) is not None:
                return [hashmap.get(remain), x]
            else:
                hashmap.update({nums[x]:x})