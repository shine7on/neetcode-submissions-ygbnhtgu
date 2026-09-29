class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prevStart, prevEnd = -1, -1
        res = []

        for start, end in intervals:
            # print(prevStart, prevEnd, start, end)
            if prevStart == -1:
                prevStart, prevEnd = start, end
            elif prevEnd >= start:
                prevEnd = max(prevEnd, end)
            else: # if new start is bigger than prev
                res.append([prevStart, prevEnd])
                prevStart, prevEnd = start, end

        if [prevStart, prevEnd] not in res:
            res.append([prevStart, prevEnd])
        return res
