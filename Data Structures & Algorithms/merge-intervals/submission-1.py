class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        minNum, maxNum = float('inf'), float('-inf')
        intervals.sort()

        for i in range(len(intervals)):
            minNum = min(minNum, intervals[i][0])
            print(minNum, maxNum)
            if maxNum < intervals[i][0] and maxNum != float('-inf'):
                res.append([minNum, maxNum])
                minNum = intervals[i][0]
            maxNum = max(maxNum, intervals[i][1])
        
        res.append([minNum, maxNum])
        
        return res
        