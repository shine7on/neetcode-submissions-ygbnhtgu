class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left,right = 1, max(piles)
        res = right

        while left <= right:
            speed = (left+right) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/speed)
            
            if hours <= h:
                res = min(res,speed)
                right = speed - 1
            else:
                left = speed + 1
        

        return res