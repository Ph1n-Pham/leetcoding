'''
https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # base case
        if n == 1:
            return nums[0] 
        
        # init array DP
        dp = [0 for _ in range(n+1)]

        # DP base cases
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        # memoization
        for i in range(3, n+1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])   # max value of whether include house i or not
    
        return dp[-1]
