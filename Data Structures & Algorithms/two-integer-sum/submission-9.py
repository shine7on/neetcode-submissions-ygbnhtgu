class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            leftover = target - nums[i]
            print(hashmap.get(leftover))
            if hashmap.get(leftover) != None:
                return [hashmap.get(leftover), i]
            hashmap[nums[i]] = i
        
        print(hashmap)