class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        res = []

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        
        items = list(hashmap.items())
        items.sort(key = lambda item : item[1], reverse = True)

        for i in range(k):
            res.append(items[i][0])
    
        return res