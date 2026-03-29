class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        curr = 1
        longest = 1
        nums = set(nums)

        for num in nums:
            prev = num - 1
            #its starting point
            if prev not in nums:
                for i in range(1,len(nums)):
                    if num+i in nums:
                        curr += 1
                    else:
                        break
                if curr > longest:
                    longest = curr
            curr = 1
        return longest