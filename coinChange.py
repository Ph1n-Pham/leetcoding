'''
https://leetcode.com/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # base cases
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # memoization
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # return only if it is not the original amount, or have a solution
        return dp[amount] if dp[amount] != amount + 1 else -1
