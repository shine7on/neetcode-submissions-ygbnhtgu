class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [ [] for x in range(len(nums)+1) ]

        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        for key, value in count.items():
            freq[value].append(key)

        result = []
        
        for x in range(len(freq)-1, 0, -1):
            for i in freq[x]:
                result.append(i)

            if len(result) == k:
                return result
        
        