'''
https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary search for O(log n)
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid

        return right
