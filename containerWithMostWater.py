'''
https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        # base case
        if n <= 1:
            return 0
        else:   # set pointers
            l, r = 0, n - 1
        
        while l < r:
            area =  (r - l) * min(heights[l], heights[r])
            res = max(area, res)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
