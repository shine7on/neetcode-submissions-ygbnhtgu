class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            heapq.heapify_max(stones)
            largest = heapq.heappop(stones)
            heapq.heapify_max(stones)
            second = heapq.heappop(stones)

            heapq.heappush(stones,largest-second)

        return 0 if not stones else stones[0]