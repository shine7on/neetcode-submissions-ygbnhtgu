class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index in range(len(nums)):
            leftover = target - nums[index]

            if leftover in hashmap:
                return [hashmap[leftover], index]

            hashmap[nums[index]] = index

        return []