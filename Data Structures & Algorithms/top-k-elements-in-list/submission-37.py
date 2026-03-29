class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        # key: number, value: count freq

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        values = list(hashmap.items())
        values.sort(key = lambda item:item[1])
        print(values)

        res = []

        for i in range(len(values)-1, len(values)-1-k, -1):
            res.append(values[i][0])

        return res

