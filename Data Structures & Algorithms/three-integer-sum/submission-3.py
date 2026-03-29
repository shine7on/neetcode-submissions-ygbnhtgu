class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # [-4,-1,-1,0,1,2]; O(nlogn) < n**2
        res = set()

        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1

            target = (-1)*nums[i]

            while left < right:
                cur = nums[left]+nums[right]
                print(target, nums[left], nums[right])
                if target == cur:
                    print(target, i,left,right)
                    res.add((nums[i],nums[left],nums[right]))
                if target < cur:
                    right -= 1
                else:
                    left += 1
            
        return list(res)
