class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = []
        for n in nums1:
            num.append(n)

        for n in nums2:
            num.append(n)

        num.sort()
        mid = len(num) // 2
        if len(num) % 2 == 1:
            return num[mid]
        return (num[mid-1] + num[mid]) / 2