class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # ??
        dp[0] = 0 # can not get 0 with any coins

        for i in range(1, amount+1):
            for j in coins:
                if i >= j:
                    dp[i] = min(1 + dp[i-j], dp[i])
                else:
                    break

        
        print(dp[amount])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
                