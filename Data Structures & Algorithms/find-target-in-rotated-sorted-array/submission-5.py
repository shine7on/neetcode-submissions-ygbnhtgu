class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (end - start) // 2 + start

            print(nums[start], nums[mid], nums[end])

            if nums[start] == target:
                return start
            elif nums[mid] == target:
                return mid
            elif nums[end] == target:
                return end
            elif target < nums[mid]:
                if nums[mid] - nums[start] < 0 or target > nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                start = mid + 1
        
        return -1
            
        