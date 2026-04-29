class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []

        for n in range(1,len(arr)):
            res.append(max(arr[n:]))
        
        res.append(-1)
        return res