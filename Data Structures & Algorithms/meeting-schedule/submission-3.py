"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda pair:pair.start)

        if intervals != []:
            prevEnd = intervals[0].end

        for i in range(1,len(intervals)):
            print(intervals[i].start, prevEnd)
            if intervals[i].start < prevEnd:
                return False
            prevEnd = intervals[i].end
        
        return True
