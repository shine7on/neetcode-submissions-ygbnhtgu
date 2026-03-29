class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0
        area = 0
        i = 0
        j = len(heights)-1

        while j > i:
            area = min(heights[i],heights[j])*(j-i)
            if max_area < area:
                max_area = area

            if(heights[i] > heights[j]):
                j -= 1
            else:
                i += 1

        return max_area

        