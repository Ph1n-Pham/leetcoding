"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        n = len(height)
        back = [0] * n
        back[n - 1] = height[n - 1]
        for i in reversed(range(n-1)):
            back[i] = max(back[i+1],height[i])
        leftmax = height[0]
        for i in range(1, n-1):
            leftmax = max(leftmax, height[i])
            diff = min(leftmax, back[i]) - height[i]
            sum += diff
        return sum


