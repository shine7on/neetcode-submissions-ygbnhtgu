class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        print(intervals)
        res = 0
        start, end = intervals[0][0], intervals[0][1]

        for i in range(1,len(intervals)):
            print(start, end, intervals[i][0], intervals[i][1])
            print(intervals[i][0] >= start, intervals[i][0] < end)
            if intervals[i][0] >= start and intervals[i][0] < end or intervals[i][1] > start and intervals[i][1] < end:
                res += 1
                if end <= intervals[i][1]: # remove i one
                    print(f'remove: {intervals[i][0], intervals[i][1]}')
                    continue
                else:
                    start = intervals[i][0]
                    end = intervals[i][1]
            start = intervals[i][0]
            end = intervals[i][1]
            
        return res
