class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_num, max_num, profit = prices[0], prices[0], 0

        for n in prices:
            if min_num > n:
                max_num, min_num = n, n
            elif max_num < n:
                max_num = n
                if profit < max_num - min_num:
                    profit  = max_num - min_num

        return profit
