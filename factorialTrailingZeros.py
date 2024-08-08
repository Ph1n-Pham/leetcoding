'''
https://leetcode.com/problems/factorial-trailing-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        power_of_five = 5
        while n >= power_of_five:
            count += n // power_of_five
            power_of_five *= 5
        return count
