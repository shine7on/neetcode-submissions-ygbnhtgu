class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 1:
            return null

        hashmap = {}

        # dictionary {num:freq}
        for num in nums:
            if num not in hashmap:
                hashmap.update({num:1})
            else:
                value = hashmap.get(num) + 1
                hashmap.update({num:value})
        
        keys = list(hashmap.keys())
        original = list(hashmap.values())
        values = list(hashmap.values())
        values.sort(reverse = True)

        k = values[:k] # freq
        result = []

        for num in range(len(k)):
            for index in range(len(hashmap.keys())):
                if k[num] == original[index]:
                    result.append(keys[index])
                    original[index] = 0
        
        return result


        