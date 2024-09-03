'''
https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

DP and Binary Search solutions
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time: O(n^2)
        # Space: O(n)

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

    def BinarySearchSolution(self, nums: List[int]) -> int:
        # Time: O(nlog(n))
        # Space: O(n)

        def binary_search(dp, target):
            left, right = 0, len(dp) - 1
            while left <= right:
                mid = (left + right) // 2
                if dp[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        dp = []
        for num in nums:
            idx = binary_search(dp, num)
            
            # if 'num' is larger than all elements in 'dp', append it.
            if idx == len(dp):
                dp.append(num)
            else:
                # otherwise, replace the element at that index with 'num'
                dp[idx] = num
        
        return len(dp)
