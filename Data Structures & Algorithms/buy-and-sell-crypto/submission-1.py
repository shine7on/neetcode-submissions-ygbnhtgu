class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        priceMin, priceMax = float('inf'), float('-inf')
        profit = 0

        for i in range(len(prices)):
            if priceMin > prices[i]:
                priceMin = prices[i]
                priceMax = float('-inf')
            elif priceMax < prices[i]:
                priceMax = prices[i]
                profit = max(priceMax - priceMin, profit)
        
        return profit
            
