class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return None

        while len(nums) > 2:
            l, r = 0, len(nums)-1
            m = round(r/2)

            print(nums[l], nums[m], nums[r])

            if nums[r] > nums[l]:
                return nums[l]
            elif nums[l] > nums[m]:
                # go to left
                nums = nums[0:m+1]
                print(nums)
            else:
                nums = nums[m+1:len(nums)]
                print(nums)
    
        return nums[0] if len(nums) == 1 or nums[0] < nums[1] else nums[1]