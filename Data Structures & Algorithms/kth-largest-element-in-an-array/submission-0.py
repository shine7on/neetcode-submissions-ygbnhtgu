class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        res = [-1001]*k
        heapq.heapify(res)
        
        for n in nums:
            if res[0] == -1001 or res[0] < n:
                heapq.heappop(res)
                heapq.heappush(res, n)
        
        return res[0]

