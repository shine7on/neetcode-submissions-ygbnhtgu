class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap {int:freq}
        hashmap = {}
        maximum = 0
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
            if hashmap[n] >= math.ceil(len(nums)/2):
                    return n