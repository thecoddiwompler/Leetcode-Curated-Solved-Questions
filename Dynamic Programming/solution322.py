# 322. Coin Change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[]
        for i in range(amount+1):
            dp.append(100000)
        dp[0]=0
        for i in range(amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i]=min(dp[i],dp[i-j]+1)
        if dp[amount]==100000:
            return -1
        return dp[amount]
