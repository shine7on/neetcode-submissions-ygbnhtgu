class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # brute force that i can think about
        for num in nums2:
            nums1.append(num)
        
        nums1.sort()
        print(nums1)

        mid = (len(nums1)-1)/2

        if type(mid) is float:
            avg = (nums1[math.ceil(mid)] + nums1[math.floor(mid)])/2
            return avg
        else:
            return nums1[mid]        