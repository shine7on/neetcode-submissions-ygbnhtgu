class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        def search(intervals,num):
            minLen = float('inf')

            for interval in intervals:
                start, end = interval
                print(start,end, num)
                if start <= num and num <= end:
                    minLen = min(end - start + 1, minLen)
            
            return minLen if minLen != float('inf') else -1

        res = []

        for query in queries:
            ans = search(intervals, query)
            res.append(ans)

        return res