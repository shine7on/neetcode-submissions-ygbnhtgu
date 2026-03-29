class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        result = []

        for k in range(len(nums)):
            target = nums[k] * -1
            i = 0
            j = len(nums) - 1

            while( i!= j and i < j):

                sum = nums[i] + nums[j]
                if (i == k or target > sum):
                    i += 1
                elif (j == k or target < sum):
                    j -= 1
                else:
                    ans = [nums[k], nums[i], nums[j]]
                    ans.sort()
                    if ans not in result:
                        result.append(ans)
                        print(f"Added: {ans}")
                    i += 1
                    j -= 1
        return list(result)