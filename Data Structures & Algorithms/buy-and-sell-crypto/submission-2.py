class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest, highest = float("inf"), 0

        for price in prices:
            if lowest > price:
                lowest = price
                highest = lowest
            elif highest < price:
                highest = price
                profit = max(profit, highest - lowest)
        
        return profit

        