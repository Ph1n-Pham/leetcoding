'''
https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150

Solve in O(log n)
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the case when n is negative
        if n < 0:
            x = 1 / x
            n = -n
        
        # Initialize the result to 1
        result = 1
        current_product = x
        
        while n > 0:
            # If n is odd, multiply the current product to the result
            if n % 2 == 1:
                result *= current_product
            
            # Square the current product for the next iteration
            current_product *= current_product
            
            # Divide n by 2
            n //= 2
        
        return result
