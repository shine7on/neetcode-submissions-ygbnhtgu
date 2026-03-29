class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l,r = 0, len(numbers) - 1
        sumN = numbers[l] + numbers[r]

        while sumN != target:
            sumN = numbers[l] + numbers[r]
            if sumN > target:
                r -= 1
            elif sumN < target:
                l += 1
        
        return [l+1,r+1]
