'''
https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # creates dp list size n filled with 0s
        dp = [0 for _ in range(n + 1)]

        # Base Cases
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # ways to reach i'th step --> step of 1 from (i - 1)th step or step of 2 from (i - 2)th step
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
