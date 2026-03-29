"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda i:i.start)
        res = []
        
        if intervals == []:
            return 0
        
        prevEnd = intervals[0].end

        for i in range(1,len(intervals)):
            print(prevEnd, intervals[i].start, intervals[i].end)
            if intervals[i].start < prevEnd:
                for j in range(len(res)):
                    if res[j] <= intervals[i].start:
                        res.remove(res[j])
                        break
                
                res.append(intervals[i].end)
            else:
                prevEnd = intervals[i].end
            print(res)
        return len(res) + 1 


        