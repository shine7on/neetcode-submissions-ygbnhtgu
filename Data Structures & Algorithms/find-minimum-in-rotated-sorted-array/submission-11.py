class Solution:
    def findMin(self, nums: List[int]) -> int:

        min_num = None
        l, r = 0, len(nums)-1
    
        while l <= r:
            m = l + int((r-l)/2)
            print(nums[l], nums[m], nums[r])

            if nums[l] <= nums[r]:
                print("case 1")
                if min_num == None or nums[l] < min_num:
                    return nums[l]
                break
            elif nums[l] > nums[m]: # search left
                r = m - 1
                min_num = nums[m]
                print("case 2")
            else: # search right
                l = m + 1
                min_num = nums[l]
                print("case 3")
        return min_num
        

        

        