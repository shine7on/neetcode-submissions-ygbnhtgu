class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1

        start, end = 0, len(nums)-1
        
        while start <= end:
            m = (start+end)//2

            if nums[m] > target:
                end = m - 1
            elif nums[m] < target:
                start = m + 1
            else:
                return m
        
        return -1
